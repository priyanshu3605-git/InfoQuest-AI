from datetime import datetime

from infoquest.schemas.document import (
    DocumentStatus,
    DocumentResponse
)

# Test 1: Valid document
doc = DocumentResponse(
    document_id="doc_001",
    filename="machine_learning.pdf",
    status=DocumentStatus.COMPLETED,
    page_count=45,
    created_at=datetime.now()
)

print("Test 1: Valid document")
print(doc.model_dump())

# Test 2: Optional page_count
doc2 = DocumentResponse(
    document_id="doc_002",
    filename="AI.pdf",
    status="pending",
    created_at=datetime.now()
)

print("\nTest 2: Optional page count")
print(doc2.model_dump())

# Test 3: Invalid status
try:
    doc3 = DocumentResponse(
        document_id="doc_003",
        filename="test.pdf",
        status="uploaded123",
        created_at=datetime.now()
    )
except Exception as e:
    print("\nTest 3: Invalid status rejected")
    print(e)