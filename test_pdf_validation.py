from io import BytesIO

from fastapi import UploadFile

from infoquest.services.pdf_validation import validate_pdf


def run_test(filename, content):

    file = UploadFile(
        filename=filename,
        file=BytesIO(content)
    )

    try:
        result = validate_pdf(file)
        print(f"{filename}: VALID")

    except ValueError as e:
        print(f"{filename}: REJECTED")
        print("Reason:", e)


# Test 1: Valid PDF signature
run_test(
    "research.pdf",
    b"%PDF-1.4\nSample content"
)

print("------------------------")


# Test 2: Image renamed as PDF
run_test(
    "image.pdf",
    b"\x89PNG\r\n\x1a\n"
)

print("------------------------")


# Test 3: Empty file
run_test(
    "empty.pdf",
    b""
)
