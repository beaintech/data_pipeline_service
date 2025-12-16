from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas import RawInput
from app.pipeline.cleaner import clean_text
from app.pipeline.store import store_record
from app.pipeline.sheets import export_to_google_sheets
from app.pipeline.pdf import generate_pdf

router = APIRouter(prefix="/pipeline", tags=["pipeline"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/clean_store")
def clean_and_store(payload: RawInput, db: Session = Depends(get_db)):
    cleaned = clean_text(payload.text, payload.source)
    record = store_record(db, cleaned)
    return {"status": "stored", "id": record.id}

@router.post("/clean_to_sheets")
def clean_to_sheets(payload: RawInput):
    cleaned = clean_text(payload.text, payload.source)
    export_to_google_sheets(cleaned)
    return {"status": "exported_to_sheets"}

@router.post("/clean_to_pdf")
def clean_to_pdf(payload: RawInput):
    cleaned = clean_text(payload.text, payload.source)
    path = f"/tmp/{payload.source}.pdf"
    generate_pdf(cleaned, path)
    return {"status": "pdf_generated", "path": path}
