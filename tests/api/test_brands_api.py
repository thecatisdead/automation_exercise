import pytest
import json
from api.brands_api import BrandsAPI


@pytest.fixture
def brands_api():
    return BrandsAPI()


# =========================================================================
# API 3: GET ALL BRANDS LIST
# =========================================================================


def test_get_all_brands_list(brands_api):
    response = brands_api.get_all_brands()

    response_data = response.json()
    assert response_data["responseCode"] == 200

    assert "brands" in response_data
    assert isinstance(response_data["brands"], list)
    assert len(response_data["brands"]) > 0

    for brand in response_data["brands"]:
        assert "id" in brand
        assert "brand" in brand


# =========================================================================
# API 4: PUT BRANDS NOW ALLOWED
# =========================================================================


def test_put_brands_not_allowed(brands_api):
    response = brands_api.put_brands_not_allowed()
    response_data = response.json()

    assert response_data["responseCode"] == 405
    assert response_data["message"] == "This request method is not supported."
