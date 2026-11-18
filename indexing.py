#!/usr/bin/env python
"""
indexing.py -- Index ShopSmart policy PDFs into ChromaDB.

Usage:
    uv run python indexing.py            # upsert (safe re-run)
    uv run python indexing.py --rebuild  # delete & rebuild the collection
"""

import sys

# Fix Windows console encoding for Unicode characters
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

from rag.config import validate_config
from rag.document_loader import load_documents
from rag.text_splitter import split_documents
from rag.vector_store import index_documents, get_collection_info


def main() -> None:
    rebuild = "--rebuild" in sys.argv

    print("=" * 60)
    print("  ShopSmart RAG -- Knowledge Base Indexing")
    print("=" * 60)

    if rebuild:
        print("\n[!] REBUILD mode: the existing collection will be deleted")
        print("    and completely re-created from the current PDFs.\n")

    # -- Step 1: Load PDFs ---------------------------------------------------
    print("\n[Step 1] Loading PDF documents ...")
    result = load_documents()

    print(f"   PDFs found:      {result.pdf_count}")
    print(f"   Pages extracted:  {result.total_pages}")
    print(f"   Empty pages:      {result.empty_pages}")
    print(f"   Usable pages:     {len(result.documents)}")

    if result.failed_pdfs:
        print(f"   [X] Failed PDFs:  {', '.join(result.failed_pdfs)}")

    if result.warnings:
        print("\n   Warnings:")
        for w in result.warnings:
            print(f"     {w}")

    # -- Step 2: Chunk documents ---------------------------------------------
    print("\n[Step 2] Splitting documents into chunks ...")
    chunks, ids = split_documents(result.documents)
    print(f"   Chunks created:   {len(chunks)}")

    # -- Step 3: Embed & index -----------------------------------------------
    print("\n[Step 3] Embedding and indexing into ChromaDB ...")
    print("   (This may take a moment on the first run while the")
    print("    embedding model is downloaded.)\n")

    summary = index_documents(chunks, ids, rebuild=rebuild)

    print(f"\n[OK] Indexing complete!")
    print(f"   Collection:       {summary['collection_name']}")
    print(f"   Persist dir:      {summary['persist_directory']}")
    print(f"   Chunks indexed:   {summary['chunks_indexed']}")
    print(f"   Source documents: {len(summary['source_documents'])}")
    for src in summary["source_documents"]:
        print(f"     - {src}")

    # -- Existing collection info --------------------------------------------
    info = get_collection_info()
    print(f"\n   Current collection size: {info['chunks_stored']} chunks")
    print()


if __name__ == "__main__":
    main()
