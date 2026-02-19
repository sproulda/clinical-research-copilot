# Clinical Research Copilot

[![Python](https://img.shields.io/badge/python-3.9-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0-green)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/docker-20.10-blue?logo=docker)](https://www.docker.com/)
[![License](https://img.shields.io/badge/license-MIT-lightgrey)](LICENSE)

**Clinical Research Copilot** is a containerized FastAPI application for ingesting, querying, and evaluating clinical research documents. The project demonstrates backend architecture, database modeling, TF-IDF embeddings, evaluation metrics, and Dockerized infrastructure for reproducible development environments.

---

## 🔹 Features

- **Document Management:** Upload, store, and retrieve clinical research documents  
- **Query System:** Retrieve top relevant document chunks using TF-IDF embeddings and cosine similarity  
- **Evaluation Metrics:** Mock hallucination detection and answer quality scoring  
- **Database:** PostgreSQL for persistent document storage  
- **Containerized Development:** Docker + Docker Compose for reproducible setup  
- **Scalable Architecture:** Separation of `models`, `services`, `routes`, and `database`  
- **API Documentation:** Swagger UI at `/docs`

---

## 🛠 Tech Stack

- **Backend:** Python 3.9, FastAPI  
- **Database:** PostgreSQL, SQLAlchemy ORM  
- **Vectorization:** Scikit-learn TF-IDF embeddings  
- **Containerization:** Docker, Docker Compose  
- **Testing / Development:** `uvicorn` hot reload, Git feature branches  

---

## 🚀 Getting Started

### Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop)  
- Git  

---

### Installation & Run

```bash
git clone https://github.com/sproulda/clinical-research-copilot.git
cd clinical-research-copilot
docker compose up --build
The API will be available at:

http://localhost:8000
Swagger docs:

http://localhost:8000/docs
Environment Variables
Create a .env file in the root (optional for TF-IDF prototype):

DATABASE_URL=postgresql://postgres:postgres@db:5432/postgres
Note: OpenAI API keys are not required for TF-IDF-based testing.

🔹 API Endpoints
1. Upload Documents
POST /documents/
Body Example:

{
  "title": "Hypertension Study 2024",
  "content": "This study evaluates beta-blockers in stage 1 hypertension...",
  "authors": ["Dr. Smith", "Dr. Lee"]
}
2. Query Documents
POST /query/
Body Example:

{
  "question": "What are the main findings about cardiovascular risk in elderly patients?"
}
Response Example:

{
  "question": "What are the main findings ...",
  "answer": "This is a mock answer generated from the top chunks.",
  "top_chunks": [
    {"text": "...", "similarity": 0.76}
  ],
  "evaluation": {
    "hallucination": {"num_sentences": 6, "num_flagged": 0, "flagged_sentences": []},
    "quality": {"answer_length_words": 63, "context_coverage_ratio": 0.69}
  }
}
🗂 Project Structure
app/
├── main.py               # FastAPI app entrypoint
├── routes/               # API routes (documents, query)
├── services/             # Business logic (document processing, embeddings, evaluation)
├── models.py             # SQLAlchemy models
├── database.py           # Engine, SessionLocal, Base
docker-compose.yml        # Compose setup for app + PostgreSQL
Dockerfile                # Docker image build for app
requirements.txt          # Python dependencies
🧪 Local Testing
Upload documents with /documents/

Query using /query/

Evaluate TF-IDF retrieval and mock metrics

Optional: run tests with pytest (if implemented)

🌟 Example Screenshots
Swagger API Docs:

Query Result Example:

Replace these URLs with actual screenshots you take locally for full effect.

🔜 Future Enhancements
Swap TF-IDF embeddings for OpenAI or other LLM embeddings

Expand evaluation scripts for real hallucination detection

Add authentication and user roles

Integrate lightweight frontend (React/Vue)

Add logging, monitoring, and CI/CD pipelines
