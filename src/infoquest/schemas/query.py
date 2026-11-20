from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class AskRequest(BaseModel):

    model_config = ConfigDict(str_strip_whitespace=True)

    question: str = Field(
        min_length=3,
        max_length=2000,
        description="Question asked by the user"
    )

    top_k: int = Field(
        default=5,
        ge=1,
        le=20,
        description="Number of relevant chunks to retrieve"
    )

    provider: Literal["ollama", "gemini"] = "ollama"
class AskResponse(BaseModel):
    message: str
    question: str
    top_k: int
    provider: Literal["ollama", "gemini"]