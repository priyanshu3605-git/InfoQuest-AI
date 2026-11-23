from pathlib import Path

from pypdf import PdfReader
from pypdf.errors import PdfReadError, FileNotDecryptedError

from infoquest.services.file_storage import DOCUMENT_STORAGE_DIR


def extract_pdf_text(filename: str) -> dict:

    # Step 1: Locate PDF
    file_path = DOCUMENT_STORAGE_DIR / Path(filename).name

    # Step 2: Check file existence
    if not file_path.exists():
        raise FileNotFoundError("PDF file not found")

    # Step 3: Read PDF safely
    try:
        reader = PdfReader(str(file_path), strict=False)

        # Step 4: Check encryption
        if reader.is_encrypted:
            raise ValueError(
                "Encrypted PDF detected. Password is required."
            )

        extracted_pages = []

        # Step 5: Extract text page by page
        for page_number, page in enumerate(reader.pages, start=1):

            text = page.extract_text()

            if text and text.strip():

                extracted_pages.append({
                    "page_number": page_number,
                    "text": text.strip()
                })

        # Step 6: Combine extracted text
        full_text = "\n\n".join(
            page["text"] for page in extracted_pages
        )

        # Step 7: Return structured result
        return {
            "total_pages": len(reader.pages),
            "extracted_pages": extracted_pages,
            "full_text": full_text,
            "has_extractable_text": bool(full_text)
        }

    except FileNotDecryptedError:
        raise ValueError("PDF is encrypted and requires a password.")

    except PdfReadError:
        raise ValueError("PDF is corrupted or cannot be read.")