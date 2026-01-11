def fixed_chunk(text: str, size: int = 500):
    return [text[i:i+size] for i in range(0, len(text), size)]

def semantic_chunk(text: str):
    paragraphs = text.split("\n\n")
    return [p.strip() for p in paragraphs if p.strip()]
