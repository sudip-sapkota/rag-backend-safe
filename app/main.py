from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env

from fastapi import FastAPI
from app.db.session import engine
from app.db.models import Base
from app.api.ingest import router as ingest_router
from app.api.chat import router as chat_router  # For conversational RAG

# Create FastAPI app
app = FastAPI(title="RAG Backend", version="0.1.0")

# Create all database tables automatically
Base.metadata.create_all(bind=engine)

# Root endpoint to check server status
@app.get("/")
def root():
    return {"message": "RAG Backend is running!"}

# Include routers
app.include_router(ingest_router, prefix="/ingest", tags=["Document Ingestion"])
app.include_router(chat_router, prefix="/chat", tags=["Conversational RAG"])  # Add chat router
