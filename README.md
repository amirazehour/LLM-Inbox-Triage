# Inbox Triage
### this project is curently only in the first development stage

A small FastAPI app that turns pasted email or message text into validated structured data: category, priority, a one-line summary, and action items. The browser sends text to the local backend; the Gemini API key stays in the server environment.

## Run locally

1. Create and activate a virtual environment, then install dependencies:

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

2. Copy `.env.example` to `.env` and add a Gemini API key.
3. Start the server:

   ```powershell
   uvicorn app.main:app --reload
   ```

4. Open <http://127.0.0.1:8000>. API docs are at <http://127.0.0.1:8000/docs>.

The `/api/triage` endpoint accepts `{"message":"..."}` and returns a `TriageResult`. Allowed categories: `action_required`, `informational`, `scheduling`, `customer_support`, `financial`, `marketing`, `other`. Priorities: `urgent`, `high`, `normal`, `low`.

## API example

```http
POST /api/triage
Content-Type: application/json

{"message":"Could you send the revised proposal by Thursday?"}
```

The UI includes Ctrl/Cmd+Enter to submit and a copy button for the result JSON.
