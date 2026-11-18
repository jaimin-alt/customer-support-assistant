"""
ChromaDB vector-store management for the ShopSmart RAG pipeline.

Handles:
* Creating / reopening the persisted collection
* Upsert-based indexing (no duplicates on re-run)
* Full rebuild with ``--rebuild``
* Summary reporting
"""

import sys
from pathlib import Path

from langchain_chroma import Chroma
from langchain_core.documents import Document

from rag.config import (
    CHROMA_COLLECTION_NAME,
    CHROMA_PERSIST_DIR,
)
from rag.embeddings import get_embedding_model


def get_vector_store() -> Chroma:
    """Return a Chroma vector store backed by the local persist directory.

    If the collection already exists on disk it is reopened;
    otherwise a new, empty collection is created.
    """
    embedding_fn = get_embedding_model()
    return Chroma(
        collection_name=CHROMA_COLLECTION_NAME,
        embedding_function=embedding_fn,
        persist_directory=CHROMA_PERSIST_DIR,
    )


def index_documents(
    chunks: list[Document],
    ids: list[str],
    *,
    rebuild: bool = False,
) -> dict:
    """Upsert *chunks* into the ChromaDB collection.

    Args:
        chunks:  Chunked ``Document`` objects with metadata.
        ids:     Parallel list of deterministic chunk IDs.
        rebuild: If ``True``, delete the existing collection first so
                 it is completely replaced.

    Returns:
        A summary dict with keys:
        ``collection_name``, ``persist_directory``,
        ``chunks_indexed``, ``source_documents``.
    """
    if rebuild:
        _delete_collection()

    store = get_vector_store()

    # Upsert in batches to avoid excessively large payloads
    batch_size = 500
    for start in range(0, len(chunks), batch_size):
        batch_chunks = chunks[start : start + batch_size]
        batch_ids = ids[start : start + batch_size]
        store.add_documents(documents=batch_chunks, ids=batch_ids)

    # Remove stale chunks whose IDs are no longer in the new set
    _remove_stale_chunks(store, set(ids))

    collection_count = store._collection.count()
    sources = {c.metadata.get("source", "unknown") for c in chunks}

    return {
        "collection_name": CHROMA_COLLECTION_NAME,
        "persist_directory": CHROMA_PERSIST_DIR,
        "chunks_indexed": collection_count,
        "source_documents": sorted(sources),
    }


def _delete_collection() -> None:
    """Delete the existing collection so it can be rebuilt."""
    try:
        store = get_vector_store()
        store.delete_collection()
        print(f"  ✓ Deleted existing collection '{CHROMA_COLLECTION_NAME}'.")
    except Exception:
        # Collection may not exist yet – that's fine
        pass


def _remove_stale_chunks(store: Chroma, current_ids: set[str]) -> None:
    """Remove chunks from the collection that are not in *current_ids*.

    This handles the case where a PDF has been updated (producing
    different chunks) or removed from the knowledge base entirely.
    """
    try:
        existing = store.get()
        if existing and existing.get("ids"):
            stale_ids = [
                eid for eid in existing["ids"] if eid not in current_ids
            ]
            if stale_ids:
                store.delete(ids=stale_ids)
                print(
                    f"  ✓ Removed {len(stale_ids)} stale chunk(s) from "
                    f"the collection."
                )
    except Exception as exc:
        print(
            f"  [WARNING] Could not check for stale chunks: {exc}",
            file=sys.stderr,
        )


def get_collection_info() -> dict:
    """Return a summary of the current persisted collection.
    
    Uses chromadb directly so we don't trigger heavy embedding model
    loading just to check the chunk count.
    """
    import chromadb
    try:
        client = chromadb.PersistentClient(path=CHROMA_PERSIST_DIR)
        coll = client.get_collection(CHROMA_COLLECTION_NAME)
        count = coll.count()
    except Exception:
        count = 0

    return {
        "collection_name": CHROMA_COLLECTION_NAME,
        "persist_directory": CHROMA_PERSIST_DIR,
        "chunks_stored": count,
    }
