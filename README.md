# Clinical Research Copilot

Clinical Research Copilot is a containerized FastAPI application for
ingesting, querying, and evaluating clinical research documents. It
demonstrates backend architecture, database modeling, TF-IDF embeddings,
evaluation metrics, and Dockerized infrastructure for reproducible
development.

------------------------------------------------------------------------

## Features

-   Upload, store, and retrieve clinical research documents
-   Query top relevant document chunks using TF-IDF embeddings
-   Mock hallucination detection and answer quality scoring
-   PostgreSQL for persistent document storage
-   Docker + Docker Compose for reproducible development
-   Clean separation of models, services, routes, and database layers

------------------------------------------------------------------------

## Tech Stack

-   Python 3.9
-   FastAPI
-   PostgreSQL
-   SQLAlchemy
-   TF-IDF (scikit-learn)
-   Docker & Docker Compose
-   Git

------------------------------------------------------------------------

## Getting Started

### Prerequisites

-   Docker Desktop
-   Git

### Installation & Run

``` bash
git clone https://github.com/sproulda/clinical-research-copilot.git
cd clinical-research-copilot
docker compose up --build
```

API base URL:

    http://localhost:8000

Swagger documentation:

    http://localhost:8000/docs

------------------------------------------------------------------------

## Environment Variables

Create a `.env` file in the root (optional for TF-IDF prototype):

``` env
DATABASE_URL=postgresql://postgres:postgres@db:5432/postgres
```

OpenAI API keys are not required for TF-IDF testing.

------------------------------------------------------------------------

## API Endpoints

### Upload Documents

    POST /documents/

Example request body:

``` json
{
  "title": "Hypertension Study 2024",
  "content": "This study evaluates beta-blockers in stage 1 hypertension...",
  "authors": ["Dr. Smith", "Dr. Lee"]
}
```

------------------------------------------------------------------------

### Query Documents

    POST /query/

Example request body:

``` json
{
  "question": "What are the main findings about cardiovascular risk in elderly patients?"
}
```

Example response:

``` json
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
```

------------------------------------------------------------------------

## Project Structure

    app/
    ├── main.py
    ├── routes/
    ├── services/
    ├── models.py
    ├── database.py
    docker-compose.yml
    Dockerfile
    requirements.txt

------------------------------------------------------------------------

## Future Improvements

-   Replace TF-IDF with real LLM embeddings
-   Add authentication and user roles
-   Add CI/CD pipeline
-   Add frontend interface
-   Add logging and monitoring

------------------------------------------------------------------------

## License

MIT License
