from fastapi.testclient import TestClient

from app.main import app
from app.models import TriageResult
from app.triage import TriageError

client = TestClient(app)


def test_triage_returns_structured_result(monkeypatch):
    expected = TriageResult(
        category="scheduling",
        priority="normal",
        summary="The sender wants to schedule a meeting.",
        action_items=["Reply with your availability."],
    )
    monkeypatch.setattr("app.main.triage_message", lambda message: expected)

    response = client.post("/api/triage", json={"message": "Can we meet tomorrow?"})

    assert response.status_code == 200
    assert response.json() == expected.model_dump(mode="json")


def test_triage_rejects_blank_message():
    response = client.post("/api/triage", json={"message": "   "})
    assert response.status_code == 422


def test_triage_reports_missing_provider_configuration(monkeypatch):
    def unavailable(_message):
        raise TriageError("AI triage is not configured.")

    monkeypatch.setattr("app.main.triage_message", unavailable)
    response = client.post("/api/triage", json={"message": "Hello"})
    assert response.status_code == 503
