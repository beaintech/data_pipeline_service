from datetime import date
from app.schemas import CleanedData

def clean_text(raw_text: str, source: str) -> CleanedData:
    return CleanedData(
        source=source,
        document_type="invoice",
        client="ACME GmbH",
        amount=1999.99,
        currency="EUR",
        document_date=date.today()
    )
