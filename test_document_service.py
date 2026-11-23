from io import BytesIO

from fastapi import UploadFile

from infoquest.services.document_service import upload_document


def test_upload(filename, content):

    file = UploadFile(
        filename=filename,
        file=BytesIO(content)
    )

    try:
        saved_filename = upload_document(file)

        print("UPLOAD SUCCESSFUL!")
        print("Original filename:", filename)
        print("Stored filename:", saved_filename)

    except ValueError as e:
        print("UPLOAD REJECTED!")
        print("Reason:", e)


# Test 1: Valid PDF
test_upload(
    "research.pdf",
    b"%PDF-1.4\nSample PDF content"
)

print("--------------------------")

# Test 2: Invalid PDF
test_upload(
    "image.pdf",
    b"Not a valid PDF"
)