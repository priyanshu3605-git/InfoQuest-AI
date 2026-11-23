from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict


class DocumentStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"


class DocumentResponse(BaseModel):
    document_id: str
    filename: str
    status: DocumentStatus

    page_count: Optional[int] = None
    title: Optional[str] = None
    author: Optional[str] = None

    created_at: datetime

    model_config = ConfigDict(from_attributes=True)