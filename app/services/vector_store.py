from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
import uuid  # <-- import UUID module

# Connect to Qdrant
client = QdrantClient(host="localhost", port=6333)

COLLECTION = "documents"

# Initialize collection safely
def init_collection():
    if COLLECTION not in [c.name for c in client.get_collections().collections]:
        client.create_collection(
            collection_name=COLLECTION,
            vectors_config=VectorParams(size=1536, distance=Distance.COSINE)
        )

# Store vector safely
def store_vector(vector, payload):
    init_collection()
    client.upsert(
        collection_name=COLLECTION,
        points=[
            {
                "id": str(uuid.uuid4()),  # <-- Use unique UUID string instead of hash
                "vector": vector,
                "payload": payload
            }
        ]
    )
