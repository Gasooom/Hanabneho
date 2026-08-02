from backend.schemas.error_response import ErrorResponse


def test_error_response():
    response = ErrorResponse(
        message="Validation failed.",
        errors=[
            "Location is required.",
            "Text is required.",
        ],
    )

    assert response.success is False
    assert response.message == "Validation failed."
    assert len(response.errors) == 2