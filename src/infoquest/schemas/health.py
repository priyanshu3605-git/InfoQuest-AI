from typing import Literal

from pydantic import BaseModel


class HomeResponse(BaseModel):
    message: str
    status: str


class HealthResponse(BaseModel):
    status: Literal["healthy"]
    application: str