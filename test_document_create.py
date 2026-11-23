from infoquest.database.connection import SessionLocal
from infoquest.database.models import DocumentModel

db = SessionLocal()

try:
    document = DocumentModel(
        document_id="doc_001",
        filename="machine_learning.pdf",
        status="completed",
        page_count=45
    )

    db.add(document)
    db.commit()

    print("Document created successfully!")

except Exception as e:
    db.rollback()
    print("Error:", e)

finally:
    db.close()