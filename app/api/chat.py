from fastapi import APIRouter, Form
from pydantic import BaseModel

router = APIRouter(prefix="/chat", tags=["Conversational RAG"])

class ChatRequest(BaseModel):
    session_id: str
    query: str

@router.post("/")
async def chat_endpoint(request: ChatRequest):
    """
    Dummy chat API for testing.
    Replace with actual RAG logic later.
    """
    return {"response": f"Received query: {request.query} for session: {request.session_id}"}
