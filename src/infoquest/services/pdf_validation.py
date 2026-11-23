from fastapi import UploadFile


def validate_pdf(file: UploadFile) -> bool:

    # Check whether filename exists
    if not file.filename:
        raise ValueError("Filename is missing")

    # Check file extension
    if not file.filename.lower().endswith(".pdf"):
        raise ValueError("Only PDF files are allowed")

    # Read the first 5 bytes
    file_signature = file.file.read(5)

    # Reset file pointer
    file.file.seek(0)

    # Check whether file is empty
    if not file_signature:
        raise ValueError("Uploaded file is empty")

    # Check PDF signature
    if file_signature != b"%PDF-":
        raise ValueError("Invalid PDF file")

    return True