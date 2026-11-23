from sqlalchemy.orm import Session

from infoquest.database.models import ChunkModel
from infoquest.services.chunking import split_text


def store_document_chunks(
    db: Session,
    document_id: str,
    text: str
) -> int:

    # Step 1: Split extracted text into chunks
    chunks = split_text(
        text,
        chunk_size=1000,
        chunk_overlap=200
    )

    # Step 2: Convert chunks into database objects
    chunk_records = []

    for index, chunk_text in enumerate(chunks):

        chunk_record = ChunkModel(
            document_id=document_id,
            chunk_index=index,
            chunk_text=chunk_text
        )

        chunk_records.append(chunk_record)

    # Step 3: Store chunks in the database
    db.add_all(chunk_records)

    # Step 4: Return the number of chunks
    return len(chunk_records)