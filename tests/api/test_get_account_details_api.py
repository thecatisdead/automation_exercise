import pytest
import json
from api.account_details_api import UserDetailsAPI

# =========================================================================
# API 14: GET USER ACCOUNT DETAIL BY EMAIL
# =========================================================================


@pytest.fixture
def get_account_details_api():
    return UserDetailsAPI()


def test_get_account_details_by_email(get_account_details_api):
    response = get_account_details_api.get_user_details_by_email(
        "junuelgetaccountdetails@gmail.com",
    )
    response_data = response.json()
    assert response_data["responseCode"] == 200
