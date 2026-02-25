from fastapi import FastAPI
from app.routes import documents, query
from app.database import engine, Base
from app import models  # ensures SQLAlchemy models are registered

app = FastAPI(title="Clinical Research Copilot")

# Create tables in the database if they don't exist
Base.metadata.create_all(bind=engine)

# Include API routers
app.include_router(documents.router)
app.include_router(query.router)

@app.get("/")
def read_root():
    return {"message": "Clinical Research Copilot is running"}