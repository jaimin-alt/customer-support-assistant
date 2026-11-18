"""
RAG chain — ties retrieval, prompt construction, and LLM generation
together for the ShopSmart customer-support assistant.
"""

import sys
from dataclasses import dataclass

from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage

from rag.config import GROQ_API_KEY, GROQ_MODEL, LLM_TEMPERATURE, validate_config
from rag.retriever import retrieve, RetrievalResult
from rag.prompts import SYSTEM_PROMPT, USER_PROMPT_TEMPLATE


@dataclass
class RAGResponse:
    """Complete response from the RAG pipeline."""

    answer: str
    sources: list[dict]  # [{"source": ..., "page_number": ...}, ...]
    retrieval_results: list[RetrievalResult]


def _build_context(results: list[RetrievalResult]) -> str:
    """Format retrieved chunks into a context string for the LLM."""
    if not results:
        return "(No relevant policy documents were found.)"

    parts: list[str] = []
    for i, r in enumerate(results, 1):
        parts.append(
            f"[Source {i}: {r.source}, page {r.page_number}]\n"
            f"{r.content}"
        )
    return "\n\n".join(parts)


def _get_llm() -> ChatGroq:
    """Create and return a ChatGroq instance."""
    validate_config()

    return ChatGroq(
        model=GROQ_MODEL,  # type: ignore[arg-type]
        api_key=GROQ_API_KEY,  # type: ignore[arg-type]
        temperature=LLM_TEMPERATURE,
        max_retries=2,
    )


def _deduplicate_sources(
    results: list[RetrievalResult],
) -> list[dict]:
    """Return unique (source, page_number) pairs preserving order."""
    seen: set[tuple[str, int]] = set()
    sources: list[dict] = []
    for r in results:
        key = (r.source, r.page_number)
        if key not in seen:
            seen.add(key)
            sources.append(
                {"source": r.source, "page_number": r.page_number}
            )
    return sources


def ask_stream(
    question: str,
    *,
    top_k: int = 4,
    debug: bool = False,
    relevance_threshold: float | None = None,
):
    """End-to-end RAG with streaming: yields tokens, returns (sources, results).

    Yields:
        str: Streaming text tokens from the LLM.

    Returns:
        tuple[list[dict], list[RetrievalResult]]: Unique cited sources and raw retrieval results.
    """
    # 1. Retrieve relevant chunks
    results = retrieve(
        question,
        top_k=top_k,
        debug=debug,
        relevance_threshold=relevance_threshold,
    )

    # 2. Build context-grounded prompt
    context = _build_context(results)
    system_msg = SystemMessage(content=SYSTEM_PROMPT.format(context=context))
    human_msg = HumanMessage(
        content=USER_PROMPT_TEMPLATE.format(question=question)
    )

    # 3. Stream from the LLM
    sources = _deduplicate_sources(results)
    try:
        llm = _get_llm()
        for chunk in llm.stream([system_msg, human_msg]):
            if chunk.content:
                yield chunk.content
    except Exception as exc:
        yield f"\n\n[ERROR] Streaming failed: {exc}"

    return sources, results


def ask(
    question: str,
    *,
    top_k: int = 4,
    debug: bool = False,
    relevance_threshold: float | None = None,
) -> RAGResponse:
    """End-to-end RAG: retrieve → build prompt → call LLM → format answer.

    Args:
        question:             The customer's question.
        top_k:                Number of chunks to retrieve.
        debug:                Print retrieval diagnostics.
        relevance_threshold:  Optional minimum relevance score.

    Returns:
        A :class:`RAGResponse` with the answer and cited sources.
    """
    # 1. Retrieve relevant chunks
    results = retrieve(
        question,
        top_k=top_k,
        debug=debug,
        relevance_threshold=relevance_threshold,
    )

    # 2. Build context-grounded prompt
    context = _build_context(results)
    system_msg = SystemMessage(content=SYSTEM_PROMPT.format(context=context))
    human_msg = HumanMessage(
        content=USER_PROMPT_TEMPLATE.format(question=question)
    )

    # 3. Call the LLM
    try:
        llm = _get_llm()
        response = llm.invoke([system_msg, human_msg])
        answer_text = response.content
    except Exception as exc:
        answer_text = (
            f"I'm sorry, I encountered an error while generating a response. "
            f"Please try again later.\n\n(Error: {exc})"
        )

    # 4. Compile source citations
    sources = _deduplicate_sources(results)

    return RAGResponse(
        answer=answer_text,  # type: ignore[arg-type]
        sources=sources,
        retrieval_results=results,
    )


def format_response(response: RAGResponse) -> str:
    """Format a RAGResponse for terminal display."""
    lines: list[str] = []
    lines.append("\nAnswer:")
    lines.append(response.answer)

    if response.sources:
        lines.append("\nSources:")
        for s in response.sources:
            lines.append(f"  - {s['source']}, page {s['page_number']}")
    else:
        lines.append(
            "\n[!] No relevant policy documents were found for this question."
        )

    return "\n".join(lines)
