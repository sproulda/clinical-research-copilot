from app.database import SessionLocal
from app.models import Document as DocumentModel
from app.services.embedding_service import create_embeddings
from app.core.logging_config import logger

def process_document(doc):
    db = SessionLocal()
    logger.info("Processing document upload")
    try:
        db_doc = DocumentModel(title=doc.title, content=doc.content)
        db.add(db_doc)
        db.commit()
        db.refresh(db_doc)

        # Generate chunks + embeddings
        create_embeddings(db_doc.id, doc.content)

    finally:
        db.close()

    return {
        "status": "saved",
        "id": db_doc.id,
        "title": db_doc.title,
        "num_characters": len(db_doc.content),
    }
