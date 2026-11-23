from fastapi import UploadFile

from infoquest.services.pdf_validation import validate_pdf
from infoquest.services.file_storage import save_uploaded_file


def upload_document(file: UploadFile) -> str:

    # Step 1: Validate uploaded PDF
    validate_pdf(file)

    # Step 2: Save the validated PDF
    saved_filename = save_uploaded_file(file)

    # Step 3: Return generated filename
    return saved_filename