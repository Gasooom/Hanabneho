from backend.utils.responses import error_response, success_response


def test_success_response():
    response = success_response(
        message="Success",
        data={"id": 1},
    )

    assert response.success is True
    assert response.message == "Success"
    assert response.data == {"id": 1}


def test_error_response():
    response = error_response(
        message="Error",
        errors=["Something went wrong"],
    )

    assert response.success is False
    assert response.message == "Error"
    assert response.errors == ["Something went wrong"]