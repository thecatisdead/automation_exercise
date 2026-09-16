import pytest
import json
from api.login_api import LoginAPI

# =========================================================================
# API 7: POST TO VERIFY LOGIN WITH VALID DETAILS
# =========================================================================


@pytest.fixture
def login_api():
    return LoginAPI()


def test_post_login_valid_details(login_api):
    response = login_api.post_login_valid_details("junueljonn@gmail.com", "password123")
    response_data = response.json()

    assert response_data["responseCode"] == 200
    assert response_data["message"] == "User exists!"


# =========================================================================
# API 8: POST TO VERIFY LOGIN WITHOUT EMAIL PARAMETER
# =========================================================================


def test_post_login_missing_param(login_api):
    response = login_api.post_login_missing_param()
    response_data = response.json()

    assert response_data["responseCode"] == 400
    assert (
        response_data["message"]
        == "Bad request, email or password parameter is missing in POST request."
    )


# =========================================================================
# API 9: DELETE TO VERIFY LOGIN
# =========================================================================


def test_delete_login(login_api):
    response = login_api.delete_login()
    response_data = response.json()

    assert response_data["responseCode"] == 405
    assert response_data["message"] == "This request method is not supported."


# =========================================================================
# API 10: POST TO VERIFY LOGIN WITH INVALID DETAILS
# =========================================================================


def test_post_invalid_details(login_api):
    response = login_api.post_login_invalid_details(
        "junueinvalid@gmail.com", "password"
    )
    response_data = response.json()

    assert response_data["responseCode"] == 404
    assert response_data["message"] == "User not found!"
