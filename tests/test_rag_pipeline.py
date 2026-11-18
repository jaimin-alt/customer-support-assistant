"""
Comprehensive tests for the ShopSmart RAG pipeline.

Test categories:
  - Document discovery and loading
  - Text chunking and metadata
  - ChromaDB persistence and idempotency
  - Retrieval quality
  - RAG chain (mocked LLM) and source citations
  - Edge cases (unsupported questions, stale chunks)

Most tests run without a real Groq API call by mocking the LLM.
Tests marked with `@pytest.mark.live` require a valid GROQ_API_KEY
and network access.

Run all offline tests:
    uv run python -m pytest tests/test_rag_pipeline.py -v

Run only live integration tests:
    uv run python -m pytest tests/test_rag_pipeline.py -v -m live
"""

import os
import shutil
import tempfile
from pathlib import Path
from unittest.mock import MagicMock, patch

try:
    pytest = __import__("pytest")
except ImportError:
    # Graceful fallback when pytest is not installed
    class _MockPytest:
        class mark:
            @staticmethod
            def live(func):
                return func

            @staticmethod
            def parametrize(*args, **kwargs):
                def decorator(func):
                    return func
                return decorator

        @staticmethod
        def fixture(*args, **kwargs):
            def decorator(func):
                return func
            return decorator

        @staticmethod
        def skip(reason=""):
            pass

    pytest = _MockPytest()  # type: ignore[assignment]

from langchain_core.documents import Document
from langchain_core.messages import AIMessage

# ── Module imports ─────────────────────────────────────────────────────
from rag.config import (
    KNOWLEDGE_BASE_DIR,
    CHROMA_COLLECTION_NAME,
    CHROMA_PERSIST_DIR,
    EMBEDDING_MODEL_NAME,
)
from rag.document_loader import discover_pdfs, load_documents, LoadResult
from rag.text_splitter import split_documents
from rag.embeddings import get_embedding_model
from rag.vector_store import get_vector_store, index_documents, get_collection_info
from rag.retriever import retrieve
from rag.rag_chain import ask, format_response, _build_context, _deduplicate_sources
from rag.retriever import RetrievalResult

# ─────────────────────────────────────────────────────────────────────────
# 15 realistic test questions spanning all policy domains
# ─────────────────────────────────────────────────────────────────────────
TEST_QUESTIONS = [
    # Returns & refunds
    "What is the return policy for electronics?",
    "How long do I have to return an item?",
    "Can I get a refund if I changed my mind?",
    # Shipping & delivery
    "How long does standard shipping take?",
    "Do you offer free shipping?",
    "What happens if my package is delayed?",
    # Order cancellation
    "Can I cancel my order after it has been shipped?",
    "How do I cancel a pending order?",
    # Payment & billing
    "What payment methods do you accept?",
    "Why was I charged twice?",
    # Warranty & product support
    "What does the warranty cover?",
    "How do I claim a warranty replacement?",
    # Damaged / missing items
    "What should I do if I received a damaged item?",
    "My order is missing an item. What do I do?",
    # Account & support
    "How do I reset my password?",
]


# ═════════════════════════════════════════════════════════════════════════
# 1. PDF Discovery
# ═════════════════════════════════════════════════════════════════════════
class TestPDFDiscovery:
    """Verify that the expected PDFs are discovered."""

    def test_discover_finds_pdfs(self):
        """At least 8 PDFs should be found in the knowledge base."""
        pdfs = discover_pdfs()
        assert len(pdfs) >= 8, (
            f"Expected ≥8 PDFs, found {len(pdfs)}: {[p.name for p in pdfs]}"
        )

    def test_all_discovered_are_pdfs(self):
        """Every discovered file must have a .pdf extension."""
        pdfs = discover_pdfs()
        for p in pdfs:
            assert p.suffix.lower() == ".pdf", f"{p.name} is not a PDF"

    def test_discover_raises_on_missing_dir(self, tmp_path):
        """Should raise FileNotFoundError for a non-existent directory."""
        with pytest.raises(FileNotFoundError):
            discover_pdfs(tmp_path / "does_not_exist")


# ═════════════════════════════════════════════════════════════════════════
# 2. Document Extraction & Chunking
# ═════════════════════════════════════════════════════════════════════════
class TestDocumentLoading:
    """Verify text extraction from PDFs."""

    def test_load_returns_documents(self):
        result = load_documents()
        assert len(result.documents) > 0, "No documents were extracted"
        assert result.pdf_count >= 8

    def test_documents_have_text(self):
        result = load_documents()
        for doc in result.documents:
            assert len(doc.page_content.strip()) > 0, (
                f"Empty content in {doc.metadata.get('source')}"
            )

    def test_metadata_is_preserved(self):
        """Every document must carry source, page, and page_number."""
        result = load_documents()
        for doc in result.documents:
            meta = doc.metadata
            assert "source" in meta, "Missing 'source' metadata"
            assert "page" in meta, "Missing 'page' metadata"
            assert "page_number" in meta, "Missing 'page_number' metadata"
            assert "category" in meta, "Missing 'category' metadata"
            assert meta["page_number"] >= 1, "page_number should be ≥ 1"


class TestTextSplitting:
    """Verify chunking and metadata propagation."""

    def test_chunks_have_metadata(self):
        result = load_documents()
        chunks, ids = split_documents(result.documents)
        assert len(chunks) > 0
        for chunk in chunks:
            assert "source" in chunk.metadata
            assert "chunk_id" in chunk.metadata
            assert "page_number" in chunk.metadata

    def test_chunk_ids_are_deterministic(self):
        """Running split_documents twice should produce identical IDs."""
        result = load_documents()
        _, ids1 = split_documents(result.documents)
        _, ids2 = split_documents(result.documents)
        assert ids1 == ids2, "Chunk IDs are not deterministic"

    def test_overlap_must_be_less_than_size(self):
        with pytest.raises(ValueError, match="smaller than"):
            split_documents([], chunk_size=100, chunk_overlap=100)

    def test_chunks_are_within_size_limit(self):
        result = load_documents()
        chunks, _ = split_documents(result.documents, chunk_size=1000)
        # Allow some tolerance since RecursiveCharacterTextSplitter
        # may occasionally produce chunks slightly over the limit
        for chunk in chunks:
            assert len(chunk.page_content) <= 1200, (
                f"Chunk too large: {len(chunk.page_content)} chars"
            )


# ═════════════════════════════════════════════════════════════════════════
# 3. ChromaDB Persistence & Idempotency
# ═════════════════════════════════════════════════════════════════════════
class TestVectorStore:
    """Verify ChromaDB persistence and upsert behaviour."""

    def test_collection_can_be_opened(self):
        """Opening the vector store should not raise."""
        store = get_vector_store()
        assert store is not None

    def test_collection_persists(self):
        """After indexing, the collection should survive reopening."""
        result = load_documents()
        chunks, ids = split_documents(result.documents)
        index_documents(chunks, ids)

        info = get_collection_info()
        assert info["chunks_stored"] > 0, "Collection is empty after indexing"

    def test_repeated_indexing_no_duplicates(self):
        """Running indexing twice should not double the chunk count."""
        result = load_documents()
        chunks, ids = split_documents(result.documents)

        index_documents(chunks, ids)
        count1 = get_collection_info()["chunks_stored"]

        index_documents(chunks, ids)
        count2 = get_collection_info()["chunks_stored"]

        assert count1 == count2, (
            f"Duplicate chunks created: {count1} → {count2}"
        )

    def test_stale_chunks_removed_on_reindex(self):
        """If a document is removed, its chunks should be cleaned up."""
        result = load_documents()
        chunks, ids = split_documents(result.documents)
        index_documents(chunks, ids)
        count_full = get_collection_info()["chunks_stored"]

        # Simulate removing half the documents
        half = len(chunks) // 2
        index_documents(chunks[:half], ids[:half])
        count_half = get_collection_info()["chunks_stored"]

        assert count_half < count_full, (
            "Stale chunks were not removed after partial re-index"
        )

    def test_rebuild_replaces_collection(self):
        """--rebuild should delete and recreate the collection."""
        result = load_documents()
        chunks, ids = split_documents(result.documents)

        index_documents(chunks, ids, rebuild=True)
        info = get_collection_info()
        assert info["chunks_stored"] == len(chunks)


# ═════════════════════════════════════════════════════════════════════════
# 4. Retrieval Quality
# ═════════════════════════════════════════════════════════════════════════
class TestRetrieval:
    """Verify that relevant chunks are retrieved for policy questions."""

    @pytest.fixture(autouse=True)
    def _ensure_indexed(self):
        """Make sure the collection is populated before retrieval tests."""
        info = get_collection_info()
        if info["chunks_stored"] == 0:
            result = load_documents()
            chunks, ids = split_documents(result.documents)
            index_documents(chunks, ids)

    def test_retrieval_returns_results(self):
        results = retrieve("What is the return policy?")
        assert len(results) > 0, "No results returned for return policy query"

    def test_retrieval_results_have_metadata(self):
        results = retrieve("How do I cancel my order?")
        for r in results:
            assert r.source, "Missing source"
            assert r.page_number >= 1, "Invalid page number"
            assert 0 <= r.relevance_score <= 1, (
                f"Score out of range: {r.relevance_score}"
            )

    def test_retrieval_relevance(self):
        """A return-policy question should retrieve from a return-related doc."""
        results = retrieve("Can I return a product for a refund?")
        sources = {r.source for r in results}
        assert any("return" in s.lower() for s in sources), (
            f"Expected a return-related source, got: {sources}"
        )

    def test_shipping_question_retrieval(self):
        results = retrieve("What are the shipping options?")
        sources = {r.source for r in results}
        assert any("shipping" in s.lower() for s in sources), (
            f"Expected a shipping-related source, got: {sources}"
        )

    @pytest.mark.parametrize("question", TEST_QUESTIONS)
    def test_all_test_questions_return_results(self, question):
        """Every test question should return at least one chunk."""
        results = retrieve(question, top_k=2)
        assert len(results) > 0, f"No results for: {question}"


# ═════════════════════════════════════════════════════════════════════════
# 5. RAG Chain (Mocked LLM)
# ═════════════════════════════════════════════════════════════════════════
class TestRAGChainMocked:
    """Test the RAG chain with a mocked LLM to avoid API calls."""

    @pytest.fixture(autouse=True)
    def _ensure_indexed(self):
        info = get_collection_info()
        if info["chunks_stored"] == 0:
            result = load_documents()
            chunks, ids = split_documents(result.documents)
            index_documents(chunks, ids)

    def _mock_llm_response(self, text: str):
        """Return a patch that makes ChatGroq.invoke return *text*."""
        mock_response = AIMessage(content=text)
        return patch(
            "rag.rag_chain.ChatGroq",
            return_value=MagicMock(invoke=MagicMock(return_value=mock_response)),
        )

    def test_answer_includes_source_citations(self):
        with self._mock_llm_response("You can return items within 30 days."):
            response = ask("What is the return policy?")
            assert len(response.sources) > 0, "No sources attached"
            formatted = format_response(response)
            assert "Sources:" in formatted

    def test_unsupported_question_no_hallucination(self):
        answer_text = (
            "I don't have enough information in our policy documents "
            "to answer that."
        )
        with self._mock_llm_response(answer_text):
            response = ask("What is the meaning of life?")
            assert "don't have enough information" in response.answer

    def test_format_response_structure(self):
        with self._mock_llm_response("Test answer."):
            response = ask("Test question")
            formatted = format_response(response)
            assert "Answer:" in formatted

    def test_context_building(self):
        """_build_context should include source references."""
        results = [
            RetrievalResult(
                content="Test content",
                source="test.pdf",
                page_number=1,
                relevance_score=0.9,
                metadata={},
            )
        ]
        context = _build_context(results)
        assert "test.pdf" in context
        assert "Test content" in context

    def test_deduplicate_sources(self):
        results = [
            RetrievalResult(
                content="A", source="a.pdf", page_number=1,
                relevance_score=0.9, metadata={},
            ),
            RetrievalResult(
                content="B", source="a.pdf", page_number=1,
                relevance_score=0.8, metadata={},
            ),
            RetrievalResult(
                content="C", source="b.pdf", page_number=2,
                relevance_score=0.7, metadata={},
            ),
        ]
        sources = _deduplicate_sources(results)
        assert len(sources) == 2  # a.pdf page 1 should appear once


# ═════════════════════════════════════════════════════════════════════════
# 6. Live Integration Test (requires GROQ_API_KEY)
# ═════════════════════════════════════════════════════════════════════════
@pytest.mark.live
class TestLiveIntegration:
    """End-to-end test that calls the real Groq API.

    Skip with:  pytest -m 'not live'
    """

    @pytest.fixture(autouse=True)
    def _ensure_indexed(self):
        info = get_collection_info()
        if info["chunks_stored"] == 0:
            result = load_documents()
            chunks, ids = split_documents(result.documents)
            index_documents(chunks, ids)

    @pytest.fixture(autouse=True)
    def _skip_without_key(self):
        if not os.getenv("GROQ_API_KEY"):
            pytest.skip("GROQ_API_KEY not set")
        if not os.getenv("GROQ_MODEL"):
            pytest.skip("GROQ_MODEL not set")

    def test_live_rag_response(self):
        response = ask("What is your return policy?")
        assert len(response.answer) > 20
        assert len(response.sources) > 0
