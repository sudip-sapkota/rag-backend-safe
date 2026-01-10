from fastapi import FastAPI
from app.api import ingest, chat
from app.db.models import Base
from app.db.session import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="RAG Backend")

app.include_router(ingest.router)
app.include_router(chat.router)
