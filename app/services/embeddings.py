import os
import random
from openai import OpenAI, OpenAIError

EMBEDDING_SIZE = 1536

def generate_embedding(text: str):
    try:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        response = client.embeddings.create(
            model="text-embedding-3-small",
            input=text
        )
        return response.data[0].embedding

    except Exception as e:
        # Fallback mock embedding (NO API COST)
        return [random.random() for _ in range(EMBEDDING_SIZE)]
