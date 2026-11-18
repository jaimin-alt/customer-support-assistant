"""
Retriever module for the ShopSmart RAG pipeline.

Wraps ChromaDB similarity search and returns results with
source metadata and relevance scores.
"""

from dataclasses import dataclass
from langchain_core.documents import Document

from rag.config import DEFAULT_TOP_K, DEFAULT_RELEVANCE_THRESHOLD
from rag.vector_store import get_vector_store


@dataclass
class RetrievalResult:
    """One retrieved chunk with its metadata and relevance score."""

    content: str
    source: str
    page_number: int
    relevance_score: float  # 0-1, higher = more relevant
    metadata: dict


def retrieve(
    query: str,
    *,
    top_k: int = DEFAULT_TOP_K,
    relevance_threshold: float | None = DEFAULT_RELEVANCE_THRESHOLD,
    debug: bool = False,
) -> list[RetrievalResult]:
    """Retrieve the most relevant chunks for *query*.

    Args:
        query:               The customer question.
        top_k:               Number of chunks to retrieve.
        relevance_threshold:  Optional minimum relevance score (0–1).
            Chunks below this threshold are discarded.  **Note:** relevance
            scores are model- and distance-function-dependent, so choose
            the threshold empirically.  ``None`` disables filtering.
        debug:               If ``True``, print retrieved chunks to stdout.

    Returns:
        A list of :class:`RetrievalResult` ordered by descending
        relevance score.
    """
    store = get_vector_store()

    # similarity_search_with_score returns (Document, distance)
    # where distance is the ChromaDB distance.
    raw_results: list[tuple[Document, float]] = (
        store.similarity_search_with_score(query, k=top_k)
    )

    results: list[RetrievalResult] = []
    for doc, dist in raw_results:
        # Convert distance to normalized similarity score [0, 1]
        # (Chroma default L2 distance: 1 / (1 + distance))
        score = 1.0 / (1.0 + max(0.0, float(dist)))

        # Apply optional threshold
        if relevance_threshold is not None and score < relevance_threshold:
            continue

        results.append(
            RetrievalResult(
                content=doc.page_content,
                source=doc.metadata.get("source", "unknown"),
                page_number=doc.metadata.get("page_number", doc.metadata.get("page", 0) + 1),
                relevance_score=round(score, 4),
                metadata=doc.metadata,
            )
        )

    if debug:
        _print_debug(query, results)

    return results


def _print_debug(query: str, results: list[RetrievalResult]) -> None:
    """Print retrieval diagnostics to the terminal."""
    print("\n" + "=" * 72)
    print(f"[DEBUG] Query: {query}")
    print(f"[DEBUG] Retrieved {len(results)} chunk(s)")
    print("=" * 72)
    for i, r in enumerate(results, 1):
        print(f"\n--- Chunk {i} ---")
        print(f"  Source:    {r.source}")
        print(f"  Page:      {r.page_number}")
        print(f"  Relevance: {r.relevance_score}")
        print(f"  Excerpt:   {r.content[:300]}...")
    print("=" * 72 + "\n")
