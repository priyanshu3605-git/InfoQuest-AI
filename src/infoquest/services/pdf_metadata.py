from pathlib import Path
from pypdf import PdfReader

from infoquest.services.file_storage import DOCUMENT_STORAGE_DIR


def extract_pdf_metadata(filename: str) -> dict:

    # Get the complete PDF path
    file_path = DOCUMENT_STORAGE_DIR / Path(filename).name

    # Check whether the file exists
    if not file_path.exists():
        raise FileNotFoundError("PDF file not found")

    # Read the PDF
    reader = PdfReader(str(file_path))

    # Extract metadata
    metadata = reader.metadata

    return {
    "page_count": len(reader.pages),
    "title": metadata.title or None if metadata else None,
    "author": metadata.author or None if metadata else None
}