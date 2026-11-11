from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.models import TriageRequest, TriageResult
from app.triage import TriageError, triage_message

app = FastAPI(title="Inbox Triage", version="1.0.0")
STATIC_DIR = Path(__file__).parent / "static"
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/", include_in_schema=False)
def index() -> FileResponse:
    return FileResponse(STATIC_DIR / "index.html")


@app.post("/api/triage", response_model=TriageResult)
def triage(request: TriageRequest) -> TriageResult:
    try:
        return triage_message(request.message.strip())
    except TriageError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc

