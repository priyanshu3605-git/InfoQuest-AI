from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from infoquest.services.chunk_service import store_document_chunks
from infoquest.schemas.query import AskRequest, AskResponse
from infoquest.schemas.health import (
    HomeResponse,
    HealthResponse
)
from infoquest.services.text_cleaner import clean_extracted_text
from infoquest.schemas.document import DocumentResponse
from infoquest.database.connection import get_db
from infoquest.database.models import DocumentModel
from fastapi import File, UploadFile
from uuid import uuid4
from infoquest.services.pdf_text_extractor import extract_pdf_text
from infoquest.services.document_service import (
    upload_document as process_document_upload
)
from infoquest.services.file_storage import delete_stored_file
from infoquest.services.pdf_metadata import extract_pdf_metadata

app = FastAPI(
    title="InfoQuest AI",
    description="An AI-powered research and knowledge discovery platform.",
    version="0.1.0"
)


# HOME ENDPOINT
@app.get("/", response_model=HomeResponse)
def home():
    return {
        "message": "Welcome to InfoQuest AI!",
        "status": "Application is running"
    }


# HEALTH CHECK ENDPOINT
@app.get("/health", response_model=HealthResponse)
def health_check():
    return {
        "status": "healthy",
        "application": "InfoQuest AI"
    }


# ASK ENDPOINT
@app.post("/ask", response_model=AskResponse)
def ask_question(request: AskRequest):

    return {
        "message": "Question received successfully",
        "question": request.question,
        "top_k": request.top_k,
        "provider": request.provider
    }


# GET ALL DOCUMENTS
@app.get("/documents", response_model=list[DocumentResponse])
def get_all_documents(db: Session = Depends(get_db)):

    documents = db.query(DocumentModel).order_by(
        DocumentModel.created_at.desc()
    ).all()

    return documents


# GET DOCUMENT BY ID
@app.get("/documents/{document_id}", response_model=DocumentResponse)
def get_document(document_id: str, db: Session = Depends(get_db)):

    document = db.query(DocumentModel).filter(
        DocumentModel.document_id == document_id
    ).first()

    if not document:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    return document


# DELETE DOCUMENT
@app.delete("/documents/{document_id}")
def delete_document(
    document_id: str,
    db: Session = Depends(get_db)
):
    document = db.query(DocumentModel).filter(
        DocumentModel.document_id == document_id
    ).first()

    if not document:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    # Save the stored filename before deleting the database record
    stored_filename = document.storage_filename

    # Delete database record
    db.delete(document)
    db.commit()

    # Delete the physical PDF file
    file_deleted = False

    if stored_filename:
        try:
            file_deleted = delete_stored_file(stored_filename)
        except OSError:
            file_deleted = False

    return {
        "message": "Document deleted successfully",
        "document_id": document_id,
        "file_deleted": file_deleted
    }

# UPLOAD DOCUMENT
@app.post(
    "/documents/upload",
    response_model=DocumentResponse,
    status_code=201
)
def upload_document_endpoint(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    saved_filename = None

    try:
        saved_filename = process_document_upload(file)

        # Extract PDF metadata
        metadata = extract_pdf_metadata(saved_filename)
        # Extract text from PDF
        text_result = extract_pdf_text(saved_filename)

        # Clean extracted text
        extracted_text = clean_extracted_text(
            text_result["full_text"]
        )
        document_id = f"doc_{uuid4().hex}"

        # Step 3: Create database record
        new_document = DocumentModel(
            document_id=document_id,
            filename=file.filename,
            storage_filename=saved_filename,
            title=metadata["title"],
            author=metadata["author"],
            status="pending",
            page_count=metadata["page_count"],
            extracted_text=extracted_text
        )     

        # Step 4: Save record to database
        # Step 1: Add the document to the database
        db.add(new_document)

# Step 2: Save the document first
        db.flush()

# Step 3: Generate and store recursive chunks
        total_chunks = store_document_chunks(
            db=db,
            document_id=document_id,
            text=extracted_text
        )

    # Step 4: Commit document and chunks together
        db.commit()

        # Step 5: Refresh document
        db.refresh(new_document)

        print(f"Successfully stored {total_chunks} chunks.")
        return new_document
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    except Exception:
        db.rollback()

        # Remove uploaded file if database operation fails
        if saved_filename:
            delete_stored_file(saved_filename)

        raise HTTPException(
            status_code=500,
            detail="Document upload failed"
        )

    finally:
        file.file.close()

