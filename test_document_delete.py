from infoquest.database.connection import SessionLocal
from infoquest.database.models import DocumentModel

db = SessionLocal()

try:
    # Find document
    document = db.query(DocumentModel).filter(
        DocumentModel.document_id == "doc_001"
    ).first()

    if document:

        # DELETE operation
        db.delete(document)

        db.commit()

        print("Document deleted successfully!")

    else:
        print("Document not found!")

except Exception as e:
    db.rollback()
    print("Database error:", e)

finally:
    db.close()