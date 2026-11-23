
from pathlib import Path
import shutil
import uuid

from fastapi import UploadFile


# Project root directory
BASE_DIR = Path(__file__).resolve().parents[3]


# Document storage directory
DOCUMENT_STORAGE_DIR = BASE_DIR / "storage" / "documents"


# Create directory automatically if it doesn't exist
DOCUMENT_STORAGE_DIR.mkdir(parents=True, exist_ok=True)


def save_uploaded_file(file: UploadFile) -> str:

    # Generate a unique filename
    unique_filename = f"{uuid.uuid4()}.pdf"

    # Create the complete file path
    file_path = DOCUMENT_STORAGE_DIR / unique_filename

    # Save uploaded file
    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Return saved filename
    return unique_filename
def delete_stored_file(filename: str) -> bool:

    # Resolve the filename safely inside storage
    file_path = DOCUMENT_STORAGE_DIR / Path(filename).name

    if file_path.exists() and file_path.is_file():
        file_path.unlink()
        return True

    return False