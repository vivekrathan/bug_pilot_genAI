
from fastapi.testclient import TestClient

from app.main import app
from app import main


client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "GenAI Bug Triage Assistant" in response.json()["message"]


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_triage():
    def fake_analysis(report):
        return {
            "summary": "The API request is failing.",
            "severity": "High",
            "severity_reason": "The reported endpoint is unavailable.",
            "affected_subsystem": "API",
            "root_cause_hypotheses": [
                "The route may not be registered correctly."
            ],
            "debugging_steps": [
                "Check the route configuration.",
                "Inspect the server logs."
            ],
            "suggested_fix": "Verify the endpoint and HTTP method.",
            "confidence": "Medium",
            "limitations": [
                "The complete stack trace was not provided."
            ],
            "similar_issues": []
        }

    main.analyze_bug_report = fake_analysis

    response = client.post(
        "/triage",
        json={
            "title": "API returns 404",
            "description": "The login endpoint returns 404.",
            "stack_trace": "",
            "environment": "Local development",
            "component": "backend"
        }
    )

    assert response.status_code == 200
    assert response.json()["severity"] == "High"
    assert len(response.json()["debugging_steps"]) > 0


def test_triage_rejects_short_title():
    response = client.post(
        "/triage",
        json={
            "title": "ab",
            "description": "This is a test description."
        }
    )

    assert response.status_code == 422
