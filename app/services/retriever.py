from qdrant_client import QdrantClient
from app.services.embeddings import generate_embedding

client = QdrantClient(host="localhost", port=6333)

COLLECTION = "documents"

def retrieve_context(query: str, limit: int = 3):
    query_vector = generate_embedding(query)

    results = client.search(
        collection_name=COLLECTION,
        query_vector=query_vector,
        limit=limit
    )

    return [hit.payload["text"] for hit in results]
