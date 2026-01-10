from fastapi import APIRouter, UploadFile, File, Form
from typing import List

router = APIRouter(prefix="/ingest", tags=["Document Ingestion"])

@router.post("/")
async def ingest_file(
    files: List[UploadFile] = File(...),
    strategy: str = Form("fixed")
):
    """
    Dummy ingest API for testing.
    Replace with actual chunking & embedding later.
    """
    return {"files_received": [file.filename for file in files], "strategy": strategy}
