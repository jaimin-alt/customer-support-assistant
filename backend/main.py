"""
FastAPI backend for the ShopSmart RAG chatbot.

Endpoints:
  POST /chat/stream   — SSE streaming response with sources
  GET  /health        — health check
"""

import json
import sys
import os
import threading
from contextlib import asynccontextmanager

# Ensure the src directory is on sys.path so `rag` package is importable
_project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_src_path = os.path.join(_project_root, "src")
if _src_path not in sys.path:
    sys.path.insert(0, _src_path)

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field

from langchain_core.messages import SystemMessage, HumanMessage

from rag.config import validate_config
from rag.embeddings import get_embedding_model
from rag.retriever import retrieve
from rag.rag_chain import _build_context, _get_llm, _deduplicate_sources
from rag.prompts import SYSTEM_PROMPT, USER_PROMPT_TEMPLATE
from rag.vector_store import get_collection_info


# ── Lifespan: warm up in background thread ─────────────────────────────────
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Start up: validate config and warm up embedding model in background."""
    validate_config()
    # Pre-warm model in background thread so server starts listening instantly
    threading.Thread(target=get_embedding_model, daemon=True).start()
    yield


# ── App setup ──────────────────────────────────────────────────────────────
app = FastAPI(
    title="ShopSmart RAG API",
    description="Customer-support chatbot powered by RAG (Retrieval-Augmented Generation).",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow Streamlit on any port
    allow_methods=["*"],
    allow_headers=["*"],
)


# ── Request / Response models ──────────────────────────────────────────────
class ChatRequest(BaseModel):
    question: str = Field(..., min_length=1, description="The user's question.")
    top_k: int = Field(4, ge=1, le=10, description="Number of chunks to retrieve.")


# ── Endpoints ──────────────────────────────────────────────────────────────
@app.get("/health")
def health():
    """Check that the vector store is ready."""
    try:
        info = get_collection_info()
        return {
            "status": "ok",
            "collection": info["collection_name"],
            "chunks_stored": info["chunks_stored"],
        }
    except Exception as exc:
        raise HTTPException(status_code=503, detail=str(exc))


@app.post("/chat/stream")
def chat_stream(request: ChatRequest):
    """
    Stream the RAG answer as Server-Sent Events (SSE).

    Event types:
      - `sources` — JSON array of {source, page_number} (sent immediately after retrieval)
      - `token`   — a streamed text chunk from the LLM
      - `error`   — error message string
      - `done`    — signals end of stream
    """
    if not request.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty.")

    def event_generator():
        try:
            # 1. Retrieve relevant chunks & deduplicate sources
            results = retrieve(request.question, top_k=request.top_k)
            sources = _deduplicate_sources(results)

            # Send sources right away so frontend knows the referenced PDFs immediately
            yield f"event: sources\ndata: {json.dumps({'sources': sources})}\n\n"

            # 2. Build context-grounded prompt
            context = _build_context(results)
            system_msg = SystemMessage(content=SYSTEM_PROMPT.format(context=context))
            human_msg = HumanMessage(
                content=USER_PROMPT_TEMPLATE.format(question=request.question)
            )

            # 3. Stream from Groq LLM
            llm = _get_llm()
            for chunk in llm.stream([system_msg, human_msg]):
                if chunk.content:
                    yield f"event: token\ndata: {json.dumps({'token': chunk.content})}\n\n"

        except Exception as exc:
            yield f"event: error\ndata: {json.dumps({'error': str(exc)})}\n\n"

        finally:
            yield "event: done\ndata: {}\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
        },
    )
