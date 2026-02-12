from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Document(BaseModel):
    title: str
    content: str
    authors: List[str]


@app.get("/")
def read_root():
    return {"message": "Clinical Research Copilot is running"}


@app.post("/documents/")
def upload_document(doc: Document):
    # For now, just simulate storage
    return {
        "status": "received",
        "title": doc.title,
        "num_characters": len(doc.content),
        "num_authors": len(doc.authors)
    }
