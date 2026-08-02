from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)


def test_create_report():
    response = client.post(
        "/api/v1/reports",
        json={
            "title": "Broken Water Pipe",
            "description": "Large water leak near the primary school.",
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["success"] is True
    assert data["message"] == "Report created successfully."

    assert data["data"]["title"] == "Broken Water Pipe"
    assert (
        data["data"]["description"]
        == "Large water leak near the primary school."
    )
    assert data["data"]["status"] == "submitted"
    assert "report_id" in data["data"]


def test_get_report():
    create_response = client.post(
        "/api/v1/reports",
        json={
            "title": "Power Outage",
            "description": "Electricity has been down for two hours.",
        },
    )

    report_id = create_response.json()["data"]["report_id"]

    response = client.get(f"/api/v1/reports/{report_id}")

    assert response.status_code == 200

    data = response.json()

    assert data["success"] is True
    assert data["data"]["report_id"] == report_id
    assert data["data"]["title"] == "Power Outage"


def test_get_unknown_report():
    response = client.get(
        "/api/v1/reports/unknown-report-id"
    )

    assert response.status_code == 404