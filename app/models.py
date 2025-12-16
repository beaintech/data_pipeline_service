from sqlalchemy import Column, Integer, String, Date, Float, DateTime
from datetime import datetime
from .database import Base

class CleanRecord(Base):
    __tablename__ = "clean_records"

    id = Column(Integer, primary_key=True, index=True)
    source = Column(String)
    document_type = Column(String)
    client = Column(String)
    amount = Column(Float)
    currency = Column(String)
    document_date = Column(Date)
    created_at = Column(DateTime, default=datetime.utcnow)
