from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from app.services.document_service import process_document

router = APIRouter()


class Document(BaseModel):
    title: str
    content: str
    authors: List[str]


@router.post("/documents/")
def upload_document(doc: Document):
    result = process_document(doc)
    return result
