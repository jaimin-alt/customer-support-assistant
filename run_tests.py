"""
run_tests.py -- Standalone test runner for the ShopSmart RAG pipeline.

Runs all tests without requiring pytest. Uses Python's built-in
unittest-compatible test discovery.

Usage:
    uv run python run_tests.py
"""

import sys
import os
import traceback
from unittest.mock import MagicMock, patch
from pathlib import Path

# Fix Windows console encoding
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

from langchain_core.documents import Document
from langchain_core.messages import AIMessage

from rag.config import KNOWLEDGE_BASE_DIR, EMBEDDING_MODEL_NAME
from rag.document_loader import discover_pdfs, load_documents
from rag.text_splitter import split_documents
from rag.embeddings import get_embedding_model
from rag.vector_store import get_vector_store, index_documents, get_collection_info
from rag.retriever import retrieve, RetrievalResult
from rag.rag_chain import ask, format_response, _build_context, _deduplicate_sources


# ── Test infrastructure ────────────────────────────────────────────────
passed = 0
failed = 0
errors: list[str] = []


def run_test(name: str, func):
    """Run a single test function and track results."""
    global passed, failed
    try:
        func()
        print(f"  [PASS] {name}")
        passed += 1
    except AssertionError as e:
        print(f"  [FAIL] {name}: {e}")
        failed += 1
        errors.append(f"FAIL: {name}: {e}")
    except Exception as e:
        print(f"  [ERROR] {name}: {type(e).__name__}: {e}")
        failed += 1
        errors.append(f"ERROR: {name}: {e}")


# ── Test Questions ─────────────────────────────────────────────────────
TEST_QUESTIONS = [
    "What is the return policy for electronics?",
    "How long do I have to return an item?",
    "Can I get a refund if I changed my mind?",
    "How long does standard shipping take?",
    "Do you offer free shipping?",
    "What happens if my package is delayed?",
    "Can I cancel my order after it has been shipped?",
    "How do I cancel a pending order?",
    "What payment methods do you accept?",
    "Why was I charged twice?",
    "What does the warranty cover?",
    "How do I claim a warranty replacement?",
    "What should I do if I received a damaged item?",
    "My order is missing an item. What do I do?",
    "How do I reset my password?",
]


# ═══════════════════════════════════════════════════════════════════════
# 1. PDF Discovery Tests
# ═══════════════════════════════════════════════════════════════════════
def test_discover_finds_pdfs():
    pdfs = discover_pdfs()
    assert len(pdfs) >= 8, f"Expected >=8 PDFs, found {len(pdfs)}"


def test_all_discovered_are_pdfs():
    pdfs = discover_pdfs()
    for p in pdfs:
        assert p.suffix.lower() == ".pdf", f"{p.name} is not a PDF"


def test_discover_raises_on_missing_dir():
    try:
        discover_pdfs(Path("C:/nonexistent_dir_12345"))
        assert False, "Should have raised FileNotFoundError"
    except FileNotFoundError:
        pass


# ═══════════════════════════════════════════════════════════════════════
# 2. Document Extraction Tests
# ═══════════════════════════════════════════════════════════════════════
def test_load_returns_documents():
    result = load_documents()
    assert len(result.documents) > 0, "No documents were extracted"
    assert result.pdf_count >= 8


def test_documents_have_text():
    result = load_documents()
    for doc in result.documents:
        assert len(doc.page_content.strip()) > 0, (
            f"Empty content in {doc.metadata.get('source')}"
        )


def test_metadata_is_preserved():
    result = load_documents()
    for doc in result.documents:
        meta = doc.metadata
        assert "source" in meta, "Missing 'source' metadata"
        assert "page" in meta, "Missing 'page' metadata"
        assert "page_number" in meta, "Missing 'page_number' metadata"
        assert "category" in meta, "Missing 'category' metadata"
        assert meta["page_number"] >= 1, "page_number should be >= 1"


# ═══════════════════════════════════════════════════════════════════════
# 3. Text Splitting Tests
# ═══════════════════════════════════════════════════════════════════════
def test_chunks_have_metadata():
    result = load_documents()
    chunks, ids = split_documents(result.documents)
    assert len(chunks) > 0
    for chunk in chunks:
        assert "source" in chunk.metadata
        assert "chunk_id" in chunk.metadata
        assert "page_number" in chunk.metadata


def test_chunk_ids_are_deterministic():
    result = load_documents()
    _, ids1 = split_documents(result.documents)
    _, ids2 = split_documents(result.documents)
    assert ids1 == ids2, "Chunk IDs are not deterministic"


def test_overlap_must_be_less_than_size():
    try:
        split_documents([], chunk_size=100, chunk_overlap=100)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass


# ═══════════════════════════════════════════════════════════════════════
# 4. Vector Store Tests
# ═══════════════════════════════════════════════════════════════════════
def test_collection_can_be_opened():
    store = get_vector_store()
    assert store is not None


def test_collection_persists():
    result = load_documents()
    chunks, ids = split_documents(result.documents)
    index_documents(chunks, ids)
    info = get_collection_info()
    assert info["chunks_stored"] > 0, "Collection is empty after indexing"


def test_repeated_indexing_no_duplicates():
    result = load_documents()
    chunks, ids = split_documents(result.documents)
    index_documents(chunks, ids)
    count1 = get_collection_info()["chunks_stored"]
    index_documents(chunks, ids)
    count2 = get_collection_info()["chunks_stored"]
    assert count1 == count2, f"Duplicates created: {count1} -> {count2}"


def test_stale_chunks_removed_on_reindex():
    result = load_documents()
    chunks, ids = split_documents(result.documents)
    index_documents(chunks, ids)
    count_full = get_collection_info()["chunks_stored"]
    half = len(chunks) // 2
    index_documents(chunks[:half], ids[:half])
    count_half = get_collection_info()["chunks_stored"]
    assert count_half < count_full, "Stale chunks were not removed"
    # Restore full index
    index_documents(chunks, ids)


def test_rebuild_replaces_collection():
    result = load_documents()
    chunks, ids = split_documents(result.documents)
    index_documents(chunks, ids, rebuild=True)
    info = get_collection_info()
    assert info["chunks_stored"] == len(chunks)


# ═══════════════════════════════════════════════════════════════════════
# 5. Retrieval Tests
# ═══════════════════════════════════════════════════════════════════════
def _ensure_indexed():
    info = get_collection_info()
    if info["chunks_stored"] == 0:
        result = load_documents()
        chunks, ids = split_documents(result.documents)
        index_documents(chunks, ids)


def test_retrieval_returns_results():
    _ensure_indexed()
    results = retrieve("What is the return policy?")
    assert len(results) > 0, "No results returned"


def test_retrieval_results_have_metadata():
    _ensure_indexed()
    results = retrieve("How do I cancel my order?")
    for r in results:
        assert r.source, "Missing source"
        assert r.page_number >= 1
        assert 0 <= r.relevance_score <= 1


def test_retrieval_relevance_returns():
    _ensure_indexed()
    results = retrieve("Can I return a product for a refund?")
    sources = {r.source for r in results}
    assert any("return" in s.lower() for s in sources), (
        f"Expected return-related source, got: {sources}"
    )


def test_retrieval_relevance_shipping():
    _ensure_indexed()
    results = retrieve("What are the shipping options?")
    sources = {r.source for r in results}
    assert any("shipping" in s.lower() for s in sources), (
        f"Expected shipping-related source, got: {sources}"
    )


def test_all_questions_return_results():
    _ensure_indexed()
    for q in TEST_QUESTIONS:
        results = retrieve(q, top_k=2)
        assert len(results) > 0, f"No results for: {q}"


# ═══════════════════════════════════════════════════════════════════════
# 6. RAG Chain (Mocked LLM) Tests
# ═══════════════════════════════════════════════════════════════════════
def test_answer_includes_source_citations():
    _ensure_indexed()
    mock_response = AIMessage(content="You can return items within 30 days.")
    with patch(
        "rag.rag_chain.ChatGroq",
        return_value=MagicMock(invoke=MagicMock(return_value=mock_response)),
    ):
        response = ask("What is the return policy?")
        assert len(response.sources) > 0, "No sources attached"
        formatted = format_response(response)
        assert "Sources:" in formatted


def test_unsupported_question_no_hallucination():
    _ensure_indexed()
    answer_text = (
        "I don't have enough information in our policy documents to answer that."
    )
    mock_response = AIMessage(content=answer_text)
    with patch(
        "rag.rag_chain.ChatGroq",
        return_value=MagicMock(invoke=MagicMock(return_value=mock_response)),
    ):
        response = ask("What is the meaning of life?")
        assert "don't have enough information" in response.answer


def test_context_building():
    results = [
        RetrievalResult(
            content="Test content", source="test.pdf", page_number=1,
            relevance_score=0.9, metadata={},
        )
    ]
    context = _build_context(results)
    assert "test.pdf" in context
    assert "Test content" in context


def test_deduplicate_sources():
    results = [
        RetrievalResult(content="A", source="a.pdf", page_number=1,
                        relevance_score=0.9, metadata={}),
        RetrievalResult(content="B", source="a.pdf", page_number=1,
                        relevance_score=0.8, metadata={}),
        RetrievalResult(content="C", source="b.pdf", page_number=2,
                        relevance_score=0.7, metadata={}),
    ]
    sources = _deduplicate_sources(results)
    assert len(sources) == 2, f"Expected 2, got {len(sources)}"


def test_format_response_structure():
    _ensure_indexed()
    mock_response = AIMessage(content="Test answer.")
    with patch(
        "rag.rag_chain.ChatGroq",
        return_value=MagicMock(invoke=MagicMock(return_value=mock_response)),
    ):
        response = ask("Test question")
        formatted = format_response(response)
        assert "Answer:" in formatted


# ═══════════════════════════════════════════════════════════════════════
# Runner
# ═══════════════════════════════════════════════════════════════════════
def main():
    print("=" * 60)
    print("  ShopSmart RAG Pipeline -- Test Suite")
    print("=" * 60)

    sections = [
        ("1. PDF Discovery", [
            ("discover_finds_pdfs", test_discover_finds_pdfs),
            ("all_discovered_are_pdfs", test_all_discovered_are_pdfs),
            ("discover_raises_on_missing_dir", test_discover_raises_on_missing_dir),
        ]),
        ("2. Document Extraction", [
            ("load_returns_documents", test_load_returns_documents),
            ("documents_have_text", test_documents_have_text),
            ("metadata_is_preserved", test_metadata_is_preserved),
        ]),
        ("3. Text Splitting", [
            ("chunks_have_metadata", test_chunks_have_metadata),
            ("chunk_ids_are_deterministic", test_chunk_ids_are_deterministic),
            ("overlap_must_be_less_than_size", test_overlap_must_be_less_than_size),
        ]),
        ("4. Vector Store", [
            ("collection_can_be_opened", test_collection_can_be_opened),
            ("collection_persists", test_collection_persists),
            ("repeated_indexing_no_duplicates", test_repeated_indexing_no_duplicates),
            ("stale_chunks_removed_on_reindex", test_stale_chunks_removed_on_reindex),
            ("rebuild_replaces_collection", test_rebuild_replaces_collection),
        ]),
        ("5. Retrieval", [
            ("retrieval_returns_results", test_retrieval_returns_results),
            ("retrieval_results_have_metadata", test_retrieval_results_have_metadata),
            ("retrieval_relevance_returns", test_retrieval_relevance_returns),
            ("retrieval_relevance_shipping", test_retrieval_relevance_shipping),
            ("all_questions_return_results", test_all_questions_return_results),
        ]),
        ("6. RAG Chain (Mocked LLM)", [
            ("answer_includes_source_citations", test_answer_includes_source_citations),
            ("unsupported_question_no_hallucination", test_unsupported_question_no_hallucination),
            ("context_building", test_context_building),
            ("deduplicate_sources", test_deduplicate_sources),
            ("format_response_structure", test_format_response_structure),
        ]),
    ]

    for section_name, tests in sections:
        print(f"\n--- {section_name} ---")
        for test_name, test_func in tests:
            run_test(test_name, test_func)

    print("\n" + "=" * 60)
    print(f"  Results: {passed} passed, {failed} failed")
    print("=" * 60)

    if errors:
        print("\nFailures:")
        for e in errors:
            print(f"  {e}")

    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()
