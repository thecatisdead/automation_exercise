import pytest
import json
from api.update_account_api import UpdateAccountAPI

# =========================================================================
# API 13: PUT METHOD TO UPDATE USER ACCOUNT
# =========================================================================


@pytest.fixture
def update_account_api():
    return UpdateAccountAPI()


def test_post_create_account(update_account_api):
    response = update_account_api.put_update_account(
        "Junuel",
        "junuelupdateaccount@gmail.com",
        "password123",
        "Mr.",
        "27",
        "07",
        "2000",
        "Junuel",
        "Dizon",
        "National ABCD Company",
        "123 Rizal Avenue",
        "Unit 5B, Mabini Building",
        "Philippines",
        "1004",
        "Metro Manila",
        "Quezon City",
        "+63 917 123 4567",
    )
    response_data = response.json()

    assert response_data["responseCode"] == 200
    assert response_data["message"] == "User updated!"
