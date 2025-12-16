# data_pipeline_service
Here is a **short, clean README** you can drop straight into GitHub.

---

# Data Pipeline Side Service

A small FastAPI side-service for n8n (or any HTTP client).
It accepts raw text, cleans it, and then either stores it in SQLite, appends a row to Google Sheets, or generates a PDF.

The workflow logic lives in n8n.
This service only exposes stable HTTP endpoints.

---

## What it does

Send JSON with `source` and `text`.

Depending on the endpoint, the service will:

* clean and store data in SQLite
* clean and export data to Google Sheets
* clean and generate a PDF file

---

## Run locally

```bash
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

Open API docs:

```
http://127.0.0.1:8000/docs
```

---

## Environment variables

```ini
DATABASE_URL=sqlite:///./pipeline.db
GOOGLE_SHEETS_ID=YOUR_SHEET_ID
GOOGLE_SERVICE_ACCOUNT_FILE=service_account.json
```

If you use Google Sheets, share the target sheet with the service account email (Editor access).

---

## API endpoints

All endpoints are under `/pipeline`.

* `POST /pipeline/clean_store`
  Cleans input and stores it in SQLite

* `POST /pipeline/clean_to_sheets`
  Cleans input and appends a row to Google Sheets

* `POST /pipeline/clean_to_pdf`
  Cleans input and generates a PDF file

### Request body

```json
{
  "source": "manual-test",
  "text": "Invoice from ACME GmbH, amount 1999.99 EUR"
}
```

---

## How to test

### Swagger UI (recommended)

Open:

```
http://127.0.0.1:8000/docs
```

Click an endpoint → Try it out → paste JSON → Execute.

---

### Curl example

```bash
curl -X POST http://127.0.0.1:8000/pipeline/clean_store \
  -H "Content-Type: application/json" \
  -d '{"source":"test","text":"sample invoice"}'
```

---

## n8n usage

Use an **HTTP Request** node in n8n:

* Method: POST
* URL: `http://<host>:8000/pipeline/<endpoint>`
* Body: JSON with `source` and `text`

This service acts as a reusable backend step inside your workflow.

---

## Notes

The cleaning logic is a placeholder.
Replace it with regex or LLM extraction without changing the API.

---

If you want, next I can:

* add a `/health` endpoint
* simplify API responses for n8n
* prepare a demo n8n workflow JSON
