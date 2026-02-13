import openai
import json
import random

from app.database import SessionLocal
from app.models import DocumentChunk

openai.api_key = "OPENAI_API_KEY"

def chunk_text(text, chunk_size=500):
    """
    Naive chunking by characters (can later improve with sentence splitting)
    """
    chunks = []
    start = 0
    while start < len(text):
        chunks.append(text[start:start+chunk_size])
        start += chunk_size
    return chunks

# OPENAPI APPROACH
# def create_embeddings(document_id, text):
#     db = SessionLocal()
#     chunks = chunk_text(text)
#     results = []

#     for chunk in chunks:
#         emb = openai.Embedding.create(
#             input=chunk,
#             model="text-embedding-3-small"
#         )
#         embedding_vector = emb['data'][0]['embedding']
#         chunk_obj = DocumentChunk(
#             document_id=document_id,
#             chunk_text=chunk,
#             embedding=json.dumps(embedding_vector)
#         )
#         db.add(chunk_obj)
#         results.append(chunk_obj)
#     db.commit()
#     db.close()
#     return results

def create_embeddings(document_id, text):
    db = SessionLocal()
    chunks = chunk_text(text)
    results = []

    for chunk in chunks:
        # Mock embedding: just random numbers
        embedding_vector = [random.random() for _ in range(1536)]
        chunk_obj = DocumentChunk(
            document_id=document_id,
            chunk_text=chunk,
            embedding=json.dumps(embedding_vector)
        )
        db.add(chunk_obj)
        results.append(chunk_obj)
    db.commit()
    db.close()
    return results
