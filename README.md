# data_pipeline_service

----
## Why this code exists (for n8n workflows)

You don’t “need” this code to make n8n work.
You need it to keep your workflow sane, reusable, and demo-ready once things stop being trivial.

### 1. What n8n is good at (and where it breaks)

n8n is excellent at:

* triggering workflows (email, webhook, upload)
* moving data between systems
* simple mapping and branching
* orchestration

n8n is not good at:

* complex parsing / cleaning logic
* validation and schema guarantees
* reusable business logic
* versioned, testable code
* anything you want to reuse across workflows

Once you put logic into Function nodes:

* it becomes copy-paste code
* it has no versioning
* it’s hard to test
* it’s painful to explain to others
* it turns into a black box

### 2. What this Python service gives you that n8n cannot

This code exists to own the logic, not the workflow.

It gives you:

* a single place where “cleaning” is defined
* strict input/output shape
* predictable behavior
* real error traces
* the ability to test logic without n8n
* something you can put on GitHub and hand to someone else

In short: **n8n calls it, but doesn’t think.**

### 3. Why n8n calls this instead of doing it itself

In the workflow, n8n should do only this:

> “I received something.
> Here is the text.
> Please process it and tell me the result.”

Everything else happens here:

* parsing
* validation
* normalization
* persistence
* export

That separation is intentional.
n8n remains replaceable. Your logic does not.

### 4. Why this matters for demos, clients, and future you

Without this service:

* every workflow duplicates logic
* small changes require editing multiple nodes
* you cannot say “this is our processing engine”
* you cannot test or debug cleanly
* you cannot reuse logic outside n8n

With this service:

* workflows become thin and readable
* logic changes in one place
* behavior is predictable
* debugging is fast
* you can run the same logic from curl, tests, or another system

This is production thinking, not over-engineering.

### 5. The mental model (key idea)

Think of it like this:

* **n8n = control plane**
* **this Python service = execution engine**

n8n decides **when** something happens.
This code decides **how** it happens.

### 6. If you removed this code tomorrow

Yes, you could:

* parse text in a Function node
* write to Sheets directly
* generate PDFs with hacks

But:

* every workflow would re-implement logic
* nothing would be reusable
* nothing would be testable
* nothing would scale
* nothing would look professional

You would have a workflow, not a system.

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
