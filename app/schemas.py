from pydantic import BaseModel
from datetime import date

class RawInput(BaseModel):
    source: str
    text: str

class CleanedData(BaseModel):
    source: str
    document_type: str
    client: str
    amount: float
    currency: str
    document_date: date
