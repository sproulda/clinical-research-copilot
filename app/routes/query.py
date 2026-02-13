from fastapi import APIRouter
from pydantic import BaseModel
from app.database import SessionLocal
from app.models import DocumentChunk
import numpy as np
import json
from app.services.evaluation_service import hallucination_check, answer_quality_score


router = APIRouter()

class QueryRequest(BaseModel):
    question: str

def chunk_similarity(question_emb, chunk_emb):
    """Cosine similarity"""
    return np.dot(question_emb, chunk_emb) / (np.linalg.norm(question_emb) * np.linalg.norm(chunk_emb))

def generate_mock_answer(question, top_chunks):
    """
    Simple grounded answer generator that stitches together top chunks.
    Keeps system deterministic and grounded.
    """
    combined_context = " ".join([c[1] for c in top_chunks])

    # Very basic heuristic answer
    return f"Based on the retrieved documents, {combined_context[:400]}"

@router.post("/query/")
def query_document(request: QueryRequest):
    db = SessionLocal()
    chunks = db.query(DocumentChunk).all()
    db.close()

    if not chunks:
        return {"error": "No document chunks available."}

    # Mock question embedding
    question_emb = np.random.rand(1536)

    # Similarity scoring
    chunks_scores = []
    for chunk in chunks:
        chunk_emb = np.array(json.loads(chunk.embedding))
        score = chunk_similarity(question_emb, chunk_emb)
        chunks_scores.append((score, chunk.chunk_text))

    # Sort and select top 3
    chunks_scores.sort(reverse=True, key=lambda x: x[0])
    top_chunks = chunks_scores[:3]

    # Generate grounded answer
    answer = generate_mock_answer(request.question, top_chunks)

    # Extract just the text for evaluation
    context_chunks = [c[1] for c in top_chunks]

    # Run evaluation
    hallucination_results = hallucination_check(answer, context_chunks)
    quality_results = answer_quality_score(answer, context_chunks)

    return {
        "question": request.question,
        "answer": answer,
        "top_chunks": [
            {"text": c[1], "similarity": c[0]} for c in top_chunks
        ],
        "evaluation": {
            "hallucination": hallucination_results,
            "quality": quality_results
        }
    }
