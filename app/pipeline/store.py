from sqlalchemy.orm import Session
from app import models
from app.schemas import CleanedData

def store_record(db: Session, data: CleanedData):
    record = models.CleanRecord(**data.dict())
    db.add(record)
    db.commit()
    db.refresh(record)
    return record
