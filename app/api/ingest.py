from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
import pdfplumber
from app.db.session import get_db
from app.db.models import Document
from app.services.chunking import fixed_chunk, semantic_chunk
from app.services.embeddings import generate_embedding
from app.services.vector_store import store_vector

router = APIRouter()

@router.post("/")
async def ingest_file(
    file: UploadFile = File(...),
    chunk_strategy: str = "default",
    db: Session = Depends(get_db)
):
    # 1. Read file
    if file.filename.endswith(".pdf"):
        text = ""
        with pdfplumber.open(file.file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
    elif file.filename.endswith(".txt"):
        text = (await file.read()).decode("utf-8")
    else:
        raise HTTPException(status_code=400, detail="Unsupported file type")

    # 2. Chunking
    if chunk_strategy == "semantic":
        chunks = semantic_chunk(text)
    else:
        chunks = fixed_chunk(text)

    # 3. Store vectors
    for chunk in chunks:
        embedding = generate_embedding(chunk)
        store_vector(
            embedding,
            {"text": chunk, "source": file.filename}
        )

    # 4. Save metadata
    doc = Document(
        filename=file.filename,
        chunk_strategy=chunk_strategy
    )
    db.add(doc)
    db.commit()

    # 5. Return response
    return {
        "filename": file.filename,
        "chunks_created": len(chunks),
        "status": "Document ingested successfully"
    }
