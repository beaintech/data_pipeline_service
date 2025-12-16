import gspread
from app.schemas import CleanedData
from app.config import settings

def export_to_google_sheets(data: CleanedData):
    gc = gspread.service_account(filename=settings.GOOGLE_SERVICE_ACCOUNT_FILE)
    sheet = gc.open_by_key(settings.GOOGLE_SHEETS_ID).sheet1

    sheet.append_row([
        data.source,
        data.document_type,
        data.client,
        data.amount,
        data.currency,
        str(data.document_date)
    ])
