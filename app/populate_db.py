from app.database import SessionLocal, Base, engine
from app.models import Document, DocumentChunk

# Drop and recreate tables
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

db = SessionLocal()

# Example: bulk documents
documents_data = [
    {
        "title": "Hypertension Study",
        "content": "Effects of beta-blockers on blood pressure.",
        "authors": ["Dr. Smith", "Dr. Lee"],
        "chunks": [
            "Beta-blockers reduce systolic BP in stage 1 patients.",
            "Study lasted 12 months with 150 participants."
        ]
    },
    {
        "title": "Diabetes Lifestyle Intervention",
        "content": "Impact of diet and exercise on insulin sensitivity.",
        "authors": ["Dr. Patel"],
        "chunks": [
            "Lifestyle intervention improved insulin sensitivity.",
            "Diet modification was key to success."
        ]
    },
    {
        "title": "Cholesterol and BMI Study",
        "content": "Correlation of cholesterol levels with BMI.",
        "authors": ["Dr. Wong", "Dr. Garcia"],
        "chunks": [
            "Cholesterol levels correlated with BMI.",
            "Adults 50-70 were analyzed over 5 years."
        ]
    },
    {
        "title": "Cancer Gene Expression",
        "content": "Gene expression in tumor vs normal tissue.",
        "authors": ["Dr. Martin"],
        "chunks": [
            "Gene expression differed in tumor vs normal tissue.",
            "Focus on breast cancer samples."
        ]
    },
    {
        "title": "Weight Loss Clinical Trial",
        "content": "Effect of combined exercise and diet.",
        "authors": ["Dr. Johnson"],
        "chunks": [
            "Exercise and diet combined led to greatest weight loss.",
            "150 subjects enrolled in randomized trial."
        ]
    }
]

# Insert documents and chunks
for doc_data in documents_data:
    doc = Document(
        title=doc_data["title"],
        content=doc_data["content"],
        authors=doc_data["authors"]
    )
    db.add(doc)
    db.flush()  # assigns doc.id so chunks can reference it

    for chunk_text in doc_data["chunks"]:
        chunk = DocumentChunk(document_id=doc.id, chunk_text=chunk_text)
        db.add(chunk)

db.commit()
db.close()

print("Database populated with sample documents and chunks!")