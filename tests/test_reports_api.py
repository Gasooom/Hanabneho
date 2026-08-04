from fastapi.testclient import TestClient

from backend.api.dependencies import analysis_service
from backend.main import app
from backend.intelligence.models.ai_analysis import AIAnalysis

client = TestClient(app)


def test_create_report():
    response = client.post(
        "/api/v1/reports",
        json={
            "title": "Water Pipeline Failure",
            "description": "Major underground water pipeline rupture causing continuous leakage and disruption to nearby neighborhoods.",
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["success"] is True
    assert data["message"] == "Report created successfully."

    assert data["data"]["title"] == "Water Pipeline Failure"
    assert (
        data["data"]["description"]
        == "Major underground water pipeline rupture causing continuous leakage and disruption to nearby neighborhoods."
    )
    assert data["data"]["status"] == "submitted"
    assert "report_id" in data["data"]


def test_get_report():
    create_response = client.post(
        "/api/v1/reports",
        json={
            "title": "Electrical Pole Fire",
            "description": "Transformer fire damaged electrical infrastructure and interrupted power supply in the surrounding area.",
        },
    )

    report_id = create_response.json()["data"]["report_id"]

    response = client.get(f"/api/v1/reports/{report_id}")

    assert response.status_code == 200

    data = response.json()

    assert data["success"] is True
    assert data["data"]["report_id"] == report_id
    assert data["data"]["title"] == "Electrical Pole Fire"


def test_get_unknown_report():
    response = client.get(
        "/api/v1/reports/unknown-report-id"
    )

    assert response.status_code == 404


def test_analyze_report_persists_dashboard_entry(monkeypatch, tmp_path):
    image = tmp_path / "bridge.jpg"
    image.write_bytes(b"fake image bytes")

    def fake_analyze(evidence):
        assert evidence.report_id
        return AIAnalysis(
            summary="Visible structural cracks detected on the bridge.",
            category="Bridge Structural Damage",
            severity="Critical",
            confidence=0.98,
            recommended_authority="Bridge Maintenance Authority",
            reasoning="Visible structural cracks detected on the bridge, creating a potential safety hazard for vehicles and pedestrians.",
        )

    monkeypatch.setattr(
        analysis_service,
        "analyze",
        fake_analyze,
    )

    response = client.post(
        "/api/v1/reports/analyze",
        files={"image": ("bridge.jpg", image.read_bytes(), "image/jpeg")},
            data={"description": "Visible structural cracks detected on the bridge, creating a potential safety hazard for vehicles and pedestrians."},
    )

    assert response.status_code == 200

    data = response.json()

    assert data["success"] is True
    assert data["data"]["category"] == "Bridge Structural Damage"

    dashboard = client.get("/api/v1/reports/dashboard")

    assert dashboard.status_code == 200

    dashboard_rows = dashboard.json()["data"]

    assert any(
        row["category"] == "Bridge Structural Damage"
        and row["description"] == "Visible structural cracks detected on the bridge, creating a potential safety hazard for vehicles and pedestrians."
        for row in dashboard_rows
    )