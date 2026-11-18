#!/usr/bin/env python
"""
rag_chat.py -- Interactive ShopSmart customer-support chatbot.

Usage:
    uv run python rag_chat.py           # normal mode
    uv run python rag_chat.py --debug   # show retrieved chunks
"""

import sys

# Fix Windows console encoding for Unicode characters
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

from rag.config import validate_config
from rag.embeddings import get_embedding_model
from rag.rag_chain import ask_stream
from rag.vector_store import get_collection_info, get_vector_store


def main() -> None:
    debug = "--debug" in sys.argv

    # Validate config before starting the session
    validate_config()

    # Check that the collection has data
    info = get_collection_info()
    if info["chunks_stored"] == 0:
        print(
            "\n[!] The vector store is empty.  Run indexing first:\n"
            "    uv run python indexing.py\n"
        )
        sys.exit(1)

    print("=" * 60)
    print("  ShopSmart Customer Support (RAG Chat)")
    print("=" * 60)
    print(f"  Collection: {info['collection_name']}")
    print(f"  Chunks:     {info['chunks_stored']}")
    if debug:
        print("  Mode:       DEBUG (retrieved chunks will be shown)")
    
    # Pre-warm embedding model and vector store so first question has no cold-start lag
    print("  Status:     Readying assistant ...", end="", flush=True)
    get_embedding_model()
    get_vector_store()
    print(" Ready!\n")

    print("  Type your question and press Enter.")
    print("  Type 'exit' or 'quit' to end the session.")
    print("=" * 60)

    while True:
        try:
            question = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n\nGoodbye!")
            break

        if not question:
            print("  (Please type a question.)")
            continue

        if question.lower() in ("exit", "quit"):
            print("\nGoodbye!")
            break

        try:
            generator = ask_stream(question, debug=debug)
            print("\nAnswer: ", end="", flush=True)
            sources = []
            
            # Consume tokens as they stream from Groq
            while True:
                try:
                    chunk = next(generator)
                    print(chunk, end="", flush=True)
                except StopIteration as stop:
                    # When generator finishes, it returns (sources, results)
                    if stop.value:
                        sources = stop.value[0]
                    break
            
            print()  # newline after answer
            
            # Print citations
            if sources:
                print("\nSources:")
                for s in sources:
                    print(f"  - {s['source']}, page {s['page_number']}")
            else:
                print("\n[!] No relevant policy documents were found for this question.")

        except Exception as exc:
            print(f"\n[ERROR] {exc}", file=sys.stderr)
            print("  Please try again or check your configuration.\n")


if __name__ == "__main__":
    main()
