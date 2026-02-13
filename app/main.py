from fastapi import FastAPI
from app.routes import documents, query
from app.database import engine, Base
from app import models
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(documents.router)
app.include_router(query.router)

@app.get("/")
def read_root():
    return {"message": "Clinical Research Copilot is running"}
