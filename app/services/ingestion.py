from fastapi import APIRouter

router = APIRouter()

@router.post("/")
async def ingest_file():
    return {"message": "File ingested successfully"}