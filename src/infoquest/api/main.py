from fastapi import FastAPI
from infoquest.schemas.query import AskRequest, AskResponse
from infoquest.schemas.health import (
    HomeResponse,
    HealthResponse
)


app = FastAPI(
    title="InfoQuest AI",
    description="An AI-powered research and knowledge discovery platform.",
    version="0.1.0"
)


@app.get("/", response_model=HomeResponse)
def home():
    return {
        "message": "Welcome to InfoQuest AI!",
        "status": "Application is running"
    }


@app.get("/health", response_model=HealthResponse)
def health_check():
    return {
        "status": "healthy",
        "application": "InfoQuest AI"
    }
@app.post("/ask", response_model=AskResponse)
def ask_question(request: AskRequest):

    return {
        "message": "Question received successfully",
        "question": request.question,
        "top_k": request.top_k,
        "provider": request.provider
    }