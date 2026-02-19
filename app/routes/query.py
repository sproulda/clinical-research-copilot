from fastapi import APIRouter
from pydantic import BaseModel
from app.database import SessionLocal
from app.models import DocumentChunk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from app.services.evaluation_service import hallucination_check, answer_quality_score

router = APIRouter()

class QueryRequest(BaseModel):
    question: str


@router.post("/query/")
def query_document(request: QueryRequest):
    db = SessionLocal()
    chunks = db.query(DocumentChunk).all()
    db.close()

    if not chunks:
        return {"error": "No document chunks found."}

    # Extract chunk texts
    chunk_texts = [chunk.chunk_text for chunk in chunks]

    # Create corpus (chunks + question)
    corpus = chunk_texts + [request.question]

    # TF-IDF vectorization
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)

    # Last vector is the question
    question_vector = tfidf_matrix[-1]
    chunk_vectors = tfidf_matrix[:-1]

    # Compute cosine similarity
    similarities = cosine_similarity(question_vector, chunk_vectors)[0]

    # Rank chunks
    ranked = sorted(
        zip(similarities, chunk_texts),
        reverse=True,
        key=lambda x: x[0]
    )

    top_chunks = ranked[:3]

    # Simple answer generation
    answer_text = " ".join([chunk[1] for chunk in top_chunks])

    # Evaluation
    hallucination_result = hallucination_check(answer_text, [c[1] for c in top_chunks])
    quality_result = answer_quality_score(answer_text, [c[1] for c in top_chunks])

    return {
        "question": request.question,
        "answer": answer_text,
        "top_chunks": [
            {"text": c[1], "similarity": float(c[0])}
            for c in top_chunks
        ],
        "evaluation": {
            "hallucination": hallucination_result,
            "quality": quality_result
        }
    }
