from infoquest.database.connection import SessionLocal
from infoquest.database.models import DocumentModel


# Create database session
db = SessionLocal()

try:
    # INSERT: Create a document
    new_document = DocumentModel(
        document_id="doc_001",
        filename="machine_learning.pdf",
        status="completed",
        page_count=45
    )

    db.add(new_document)
    db.commit()
    db.refresh(new_document)

    print("Document inserted successfully!")

    # Display inserted document
    print("\nInserted Document:")
    print("ID:", new_document.id)
    print("Document ID:", new_document.document_id)
    print("Filename:", new_document.filename)
    print("Status:", new_document.status)
    print("Pages:", new_document.page_count)

    # SELECT: Retrieve document
    retrieved_document = db.query(DocumentModel).filter(
        DocumentModel.document_id == "doc_001"
    ).first()

    print("\nRetrieved Document:")
    print(retrieved_document.filename)

except Exception as e:
    db.rollback()
    print("Database error:", e)

finally:
    db.close()