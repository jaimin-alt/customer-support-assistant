"""
Text chunking for the ShopSmart RAG pipeline.

Uses LangChain's RecursiveCharacterTextSplitter to break extracted
document pages into overlapping chunks suitable for embedding.

**Why chunking?**
Embedding models have a fixed context window (all-MiniLM-L6-v2 handles
up to 256 word-piece tokens).  Entire policy documents vastly exceed
that limit, so each document must be split into smaller passages whose
embeddings capture focused semantic meaning.  Smaller chunks also
improve retrieval precision: a query about "refund timelines" should
match the specific paragraph that discusses timelines, not a 10-page
document that happens to mention them somewhere.

**Why overlap?**
Policy rules often span paragraph boundaries.  An overlap of 150
characters means the end of one chunk is duplicated at the start of the
next, reducing the chance that a critical condition or deadline is split
between chunks and lost from the retrieval result.

Chunk IDs
---------
Every chunk receives a deterministic ID of the form
``<source_filename>::page<N>::chunk<M>`` so the same document always
produces the same IDs.  This enables upsert-style indexing without
duplication.
"""

import hashlib
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from rag.config import DEFAULT_CHUNK_SIZE, DEFAULT_CHUNK_OVERLAP


def _make_chunk_id(source: str, page: int, chunk_index: int) -> str:
    """Return a stable, deterministic chunk identifier.

    The ID is built from the source filename, page number, and the
    chunk's ordinal position within that page.
    """
    raw = f"{source}::page{page}::chunk{chunk_index}"
    return raw


def split_documents(
    documents: list[Document],
    chunk_size: int = DEFAULT_CHUNK_SIZE,
    chunk_overlap: int = DEFAULT_CHUNK_OVERLAP,
) -> tuple[list[Document], list[str]]:
    """Split *documents* into overlapping chunks with stable IDs.

    Args:
        documents: Page-level ``Document`` objects produced by the
                   document loader.
        chunk_size: Target maximum characters per chunk.
        chunk_overlap: Characters of overlap between consecutive chunks.

    Returns:
        A 2-tuple ``(chunks, ids)`` where *chunks* is a list of
        ``Document`` objects and *ids* is a parallel list of
        deterministic string IDs suitable for ChromaDB upsert.

    Raises:
        ValueError: If *chunk_overlap* ≥ *chunk_size*.
    """
    if chunk_overlap >= chunk_size:
        raise ValueError(
            f"chunk_overlap ({chunk_overlap}) must be smaller than "
            f"chunk_size ({chunk_size})."
        )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        is_separator_regex=False,
    )

    chunks: list[Document] = []
    ids: list[str] = []

    # Track per-source-page chunk counters so IDs are deterministic
    page_chunk_counter: dict[str, int] = {}

    for doc in documents:
        source = doc.metadata.get("source", "unknown")
        page = doc.metadata.get("page", 0)

        page_key = f"{source}::page{page}"

        sub_chunks = splitter.split_documents([doc])

        for sub in sub_chunks:
            idx = page_chunk_counter.get(page_key, 0)
            page_chunk_counter[page_key] = idx + 1

            chunk_id = _make_chunk_id(source, page, idx)

            # Carry forward all original metadata plus chunk-level info
            sub.metadata.update(
                {
                    "chunk_id": chunk_id,
                    "chunk_index": idx,
                }
            )

            chunks.append(sub)
            ids.append(chunk_id)

    return chunks, ids
