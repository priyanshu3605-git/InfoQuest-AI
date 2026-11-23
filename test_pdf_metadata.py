from infoquest.services.file_storage import save_uploaded_file
from infoquest.services.pdf_metadata import extract_pdf_metadata

from fastapi import UploadFile
from io import BytesIO


# Upload a real PDF file for testing
with open("24156133 DMDW Assignment.pdf", "rb") as pdf:
    upload = UploadFile(
        filename="24156133 DMDW Assignment.pdf",
        file=BytesIO(pdf.read())
    )

    saved_filename = save_uploaded_file(upload)


# Extract metadata
metadata = extract_pdf_metadata(saved_filename)

print("PDF Metadata:")
print(metadata)