import redis
import json
import os

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

def get_history(session_id: str):
    data = redis_client.get(session_id)
    return json.loads(data) if data else []

def save_history(session_id: str, role: str, content: str):
    history = get_history(session_id)
    history.append({"role": role, "content": content})
    redis_client.set(session_id, json.dumps(history))
