from infoquest.database.connection import SessionLocal
from infoquest.database.models import DocumentModel

db = SessionLocal()

try:
    # Find existing document
    document = db.query(DocumentModel).filter(
        DocumentModel.document_id == "doc_001"
    ).first()

    if document:
        # UPDATE operation
        document.status = "processing"

        db.commit()
        db.refresh(document)

        print("Document updated successfully!")
        print("New status:", document.status)

    else:
        print("Document not found!")

except Exception as e:
    db.rollback()
    print("Database error:", e)

finally:
    db.close()