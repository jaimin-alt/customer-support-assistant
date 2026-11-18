"""
Centralized configuration for the ShopSmart RAG pipeline.

Loads settings from .env and provides validated configuration
for all pipeline components. Every tunable parameter lives here
so nothing is scattered across modules.
"""

import os
import sys
from pathlib import Path

from dotenv import load_dotenv

# ── Project paths ──────────────────────────────────────────────────────────
# Resolve relative to the project root (two levels up from this file)
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
KNOWLEDGE_BASE_DIR = PROJECT_ROOT / "knowledge-base" / "pdf"
CHROMA_PERSIST_DIR = str(PROJECT_ROOT / "chroma_db")

# ── Load .env from project root ───────────────────────────────────────────
_dotenv_path = PROJECT_ROOT / ".env"
if _dotenv_path.exists():
    load_dotenv(_dotenv_path)
else:
    print(f"[WARNING] .env file not found at {_dotenv_path}", file=sys.stderr)

# ── Groq / LLM configuration ──────────────────────────────────────────────
GROQ_API_KEY: str | None = os.getenv("GROQ_API_KEY")
GROQ_MODEL: str | None = os.getenv("GROQ_MODEL")

# ── Embedding model ───────────────────────────────────────────────────────
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

# ── ChromaDB ──────────────────────────────────────────────────────────────
CHROMA_COLLECTION_NAME = "shopsmart_knowledge"

# ── Text splitting defaults ───────────────────────────────────────────────
DEFAULT_CHUNK_SIZE = 1_000
DEFAULT_CHUNK_OVERLAP = 150

# ── Retrieval defaults ────────────────────────────────────────────────────
DEFAULT_TOP_K = 4
DEFAULT_RELEVANCE_THRESHOLD: float | None = None  # disabled by default

# ── LLM defaults ──────────────────────────────────────────────────────────
LLM_TEMPERATURE = 0


def validate_config() -> None:
    """Validate that all required configuration is present.

    Raises SystemExit with an actionable message when something is wrong.
    """
    errors: list[str] = []

    if not GROQ_API_KEY:
        errors.append(
            "GROQ_API_KEY is not set. "
            "Add it to your .env file:  GROQ_API_KEY=gsk_..."
        )

    if not GROQ_MODEL:
        errors.append(
            "GROQ_MODEL is not set. "
            "Add a currently supported Groq chat model to your .env file, e.g.:\n"
            "  GROQ_MODEL=openai/gpt-oss-20b\n"
            "Check https://console.groq.com/docs/models for available models."
        )

    if not KNOWLEDGE_BASE_DIR.exists():
        errors.append(
            f"Knowledge-base directory not found: {KNOWLEDGE_BASE_DIR}\n"
            "Create it and place your ShopSmart PDF policy documents inside."
        )

    if errors:
        print("\n[CONFIGURATION ERROR]", file=sys.stderr)
        for i, err in enumerate(errors, 1):
            print(f"  {i}. {err}", file=sys.stderr)
        sys.exit(1)
