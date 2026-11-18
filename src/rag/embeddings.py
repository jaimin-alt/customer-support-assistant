"""
Embedding model initialisation for the ShopSmart RAG pipeline.

Provides a single factory function that returns a
HuggingFaceEmbeddings instance configured with the
``sentence-transformers/all-MiniLM-L6-v2`` model.

The same instance must be used during both indexing and querying
to ensure vector-space compatibility.
"""

import sys

from langchain_huggingface import HuggingFaceEmbeddings

from rag.config import EMBEDDING_MODEL_NAME

# Module-level cache so the model is loaded at most once per process.
_cached_embeddings: HuggingFaceEmbeddings | None = None


def get_embedding_model() -> HuggingFaceEmbeddings:
    """Return a cached ``HuggingFaceEmbeddings`` instance.

    Tries loading from local cache first (local_files_only=True) to avoid
    DNS lookup lags when offline. If not cached, downloads weights.

    Returns:
        A ready-to-use HuggingFaceEmbeddings instance.
    """
    global _cached_embeddings

    if _cached_embeddings is not None:
        return _cached_embeddings

    # Try local cache first for sub-second startup
    try:
        _cached_embeddings = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL_NAME,
            model_kwargs={"device": "cpu", "local_files_only": True},
            encode_kwargs={"normalize_embeddings": True},
        )
        return _cached_embeddings
    except Exception:
        pass

    try:
        _cached_embeddings = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL_NAME,
            model_kwargs={"device": "cpu"},
            encode_kwargs={"normalize_embeddings": True},
        )
        return _cached_embeddings

    except Exception as exc:
        print(
            f"\n[EMBEDDING ERROR] Failed to initialise the embedding model "
            f"'{EMBEDDING_MODEL_NAME}'.\n"
            f"  Detail: {exc}\n\n"
            "If this is the first run, ensure you have internet access so\n"
            "the model weights can be downloaded.\n"
            "If the 'sentence-transformers' package is missing, run:\n"
            "  uv add sentence-transformers",
            file=sys.stderr,
        )
        sys.exit(1)
