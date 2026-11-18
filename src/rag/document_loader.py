"""
PDF document loader for the ShopSmart knowledge base.

Discovers, loads, and validates PDF files from the knowledge-base
directory.  Reports extraction failures, empty pages, and potential
OCR-only documents instead of silently ignoring them.
"""

import re
from pathlib import Path
from dataclasses import dataclass, field

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document

from rag.config import KNOWLEDGE_BASE_DIR


@dataclass
class LoadResult:
    """Aggregated result of loading all PDFs."""

    documents: list[Document] = field(default_factory=list)
    pdf_count: int = 0
    total_pages: int = 0
    empty_pages: int = 0
    failed_pdfs: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


def _normalize_text(text: str) -> str:
    """Collapse excessive whitespace while preserving paragraph breaks."""
    # Replace runs of spaces/tabs (not newlines) with a single space
    text = re.sub(r"[^\S\n]+", " ", text)
    # Collapse three-or-more consecutive newlines into two
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def _infer_category(filename: str) -> str:
    """Derive a human-readable category from the PDF filename."""
    stem = Path(filename).stem
    return stem.replace("_", " ").title()


def discover_pdfs(directory: Path | None = None) -> list[Path]:
    """Return a sorted list of PDF file paths in *directory*.

    Args:
        directory: Folder to scan.  Defaults to the configured
                   KNOWLEDGE_BASE_DIR.

    Returns:
        Sorted list of Path objects for every ``*.pdf`` file found.

    Raises:
        FileNotFoundError: If the directory does not exist.
    """
    directory = directory or KNOWLEDGE_BASE_DIR
    if not directory.exists():
        raise FileNotFoundError(
            f"Knowledge-base directory not found: {directory}"
        )

    pdfs = sorted(directory.glob("*.pdf"))
    return pdfs


def load_documents(directory: Path | None = None) -> LoadResult:
    """Load and validate all PDFs from the knowledge base.

    Each page becomes a separate ``Document`` carrying metadata:

    * ``source``          – the PDF filename (e.g. ``return_refund_policy.pdf``)
    * ``source_path``     – relative path from the project root
    * ``page``            – 0-based page index as stored by PyPDFLoader
    * ``page_number``     – 1-based human-readable page number
    * ``category``        – inferred from the filename
    * ``total_pages``     – total pages in that PDF

    Empty pages (fewer than 20 non-whitespace characters) are dropped
    and counted in :pyattr:`LoadResult.empty_pages`.

    Returns:
        A :class:`LoadResult` summarising what was loaded.

    Raises:
        ValueError: If no usable documents could be extracted.
    """
    directory = directory or KNOWLEDGE_BASE_DIR
    result = LoadResult()
    pdf_paths = discover_pdfs(directory)

    if not pdf_paths:
        raise ValueError(
            f"No PDF files found in {directory}. "
            "Place your ShopSmart policy PDFs there."
        )

    for pdf_path in pdf_paths:
        result.pdf_count += 1
        filename = pdf_path.name
        relative_path = str(pdf_path.relative_to(pdf_path.parent.parent.parent))
        category = _infer_category(filename)

        try:
            loader = PyPDFLoader(str(pdf_path))
            pages: list[Document] = loader.load()
        except Exception as exc:
            result.failed_pdfs.append(filename)
            result.warnings.append(
                f"[ERROR] Failed to load '{filename}': {exc}"
            )
            continue

        if not pages:
            result.failed_pdfs.append(filename)
            result.warnings.append(
                f"[WARNING] '{filename}' produced zero pages – "
                "it may be an image-based (scanned) PDF that requires OCR."
            )
            continue

        pdf_has_text = False
        for page_doc in pages:
            result.total_pages += 1
            raw_text = page_doc.page_content or ""
            cleaned = _normalize_text(raw_text)

            # Heuristic: fewer than 20 non-whitespace chars ≈ empty page
            if len(cleaned.replace(" ", "").replace("\n", "")) < 20:
                result.empty_pages += 1
                result.warnings.append(
                    f"[INFO] '{filename}' page {page_doc.metadata.get('page', '?')+1} "
                    "has little or no extractable text (skipped)."
                )
                continue

            pdf_has_text = True
            # Build enriched metadata
            page_idx = page_doc.metadata.get("page", 0)
            page_doc.page_content = cleaned
            page_doc.metadata.update(
                {
                    "source": filename,
                    "source_path": relative_path,
                    "page": page_idx,
                    "page_number": page_idx + 1,  # human-readable
                    "category": category,
                    "total_pages": len(pages),
                }
            )
            result.documents.append(page_doc)

        if not pdf_has_text:
            result.warnings.append(
                f"[WARNING] '{filename}' contains {len(pages)} page(s) but none "
                "had usable text – it may be a scanned/image-only PDF requiring OCR."
            )

    if not result.documents:
        raise ValueError(
            "No usable text was extracted from any PDF in "
            f"{directory}.  Check that the files are text-based PDFs."
        )

    return result
