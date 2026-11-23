from infoquest.services.pdf_text_extractor import extract_pdf_text
from infoquest.services.file_storage import DOCUMENT_STORAGE_DIR


# Find an existing uploaded PDF
pdf_files = list(DOCUMENT_STORAGE_DIR.glob("*.pdf"))

if not pdf_files:
    print("No PDF files found in storage.")
else:

    # Select the first available PDF
    pdf_filename = pdf_files[0].name

    print("Testing PDF:", pdf_filename)

    # Extract PDF text
    result = extract_pdf_text(pdf_filename)

    # Display results
    print("\nTotal Pages:", result["total_pages"])

    print("\nExtracted Pages:")

    for page in result["extracted_pages"]:
        print("\nPage:", page["page_number"])
        print(page["text"][:500])

    print("\nHas Extractable Text:", result["has_extractable_text"])