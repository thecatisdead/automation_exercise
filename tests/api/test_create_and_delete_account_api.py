import pytest
import json
from api.create_account_api import CreateAPI, DeleteAPI

# =========================================================================
# API 11: POST TO CREATE/REGISTER USER ACCOUNT
# =========================================================================


@pytest.fixture
def create_account_api():
    return CreateAPI()


def test_post_create_account(create_account_api):
    response = create_account_api.post_create_account(
        "Junuel",
        "junuelcreateaccount88@gmail.com",
        "password123",
        "Mr.",
        "27",
        "07",
        "2000",
        "Junuel",
        "Dizon",
        "National ABD Company",
        "1234 Rizal Avenue",
        "Unit 5B, Mabini Building",
        "Philippines",
        "1004",
        "Metro Manila",
        "Quezon City",
        "+63 917 123 4567",
    )
    response_data = response.json()

    assert response_data["responseCode"] == 201
    assert response_data["message"] == "User created!"


# =========================================================================
# API 12: DELETE METHOD TO DELETE USER ACCOUNT
# =========================================================================


@pytest.fixture
def delete_created_account_api():
    return DeleteAPI()


def test_delete_created_account(delete_created_account_api):
    response = delete_created_account_api.delete_created_account(
        "junuelcreateaccount88@gmail.com", "password123"
    )
    response_data = response.json()

    assert response_data["responseCode"] == 200
    assert response_data["message"] == "Account deleted!"
