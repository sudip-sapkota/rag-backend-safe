from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.services.generate_answer import generate_answer
from app.api.chat_memory import get_history, add_to_history

router = APIRouter()

class ChatRequest(BaseModel):
    query: str

@router.post("/")
def chat_endpoint(request: ChatRequest):
    # Fetch context from ingested documents (RAG retrieval)
    context = ["This is a dummy context from PDF"]  # replace with real retrieval
    history = get_history()  # retrieve previous chat from Redis
    
    answer = generate_answer(request.query, context, history)
    
    add_to_history({"role": "user", "content": request.query})
    add_to_history({"role": "assistant", "content": answer})
    
    return {"response": answer}
