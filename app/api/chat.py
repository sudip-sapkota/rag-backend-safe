from fastapi import APIRouter
from pydantic import BaseModel
from app.services.generate_answer import generate_answer
import redis
import os
import json

# ---------------------------
# Redis setup (chat memory)
# ---------------------------
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
CHAT_KEY = "chat_history"

def get_history() -> list:
    history_json = r.get(CHAT_KEY)
    if history_json:
        return json.loads(history_json)
    return []

def add_to_history(message: dict):
    history = get_history()
    history.append(message)
    r.set(CHAT_KEY, json.dumps(history))

# ---------------------------
# FastAPI router
# ---------------------------
router = APIRouter()

class ChatRequest(BaseModel):
    query: str

@router.post("/")
def chat_endpoint(request: ChatRequest):
    # Fetch context from uploaded documents (replace with real retrieval later)
    context = ["This is a dummy context from uploaded PDFs"]  

    # Get chat history from Redis
    history = get_history()

    # Generate answer
    answer = generate_answer(request.query, context, history)

    # Save conversation
    add_to_history({"role": "user", "content": request.query})
    add_to_history({"role": "assistant", "content": answer})

    return {"response": answer}
