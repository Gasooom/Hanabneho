from backend.schemas.api_response import ApiResponse


def test_api_response():
    response = ApiResponse(
        success=True,
        message="Success",
        data={"report_id": "RPT-001"},
    )

    assert response.success is True
    assert response.message == "Success"
    assert response.data["report_id"] == "RPT-001"