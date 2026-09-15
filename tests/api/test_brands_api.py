import pytest
import json
from api.brands_api import BrandsAPI


@pytest.fixture
def brands_api():
    return BrandsAPI()


# =========================================================================
# API 3: GET ALL BRANDS LIST
# =========================================================================


# def test_get_all_brands_list(brands_api):
#     response = brands_api.get_all_brands()

#     print("Status:", response.status_code)
#     print("Headers:", response.headers)
#     print("Body:", json.dumps(response.json()))

#     assert response.status_code == 200

#     response_data = response.json()
#     assert "brands" in response_data
#     assert isinstance(response_data["brands"], list)
#     assert len(response_data["brands"]) > 0

#     # first_product = response_data["brands"][0]
#     # assert "id" in first_product
#     # assert "name" in first_product
#     # assert "price" in first_product
#     # assert "brand" in first_product
#     # assert "category" in


# =========================================================================
# API 4: PUT BRANDS NOW ALLOWED
# =========================================================================


def test_put_brands_not_allowed(brands_api):
    response = brands_api.put_brands_not_allowed()
    response_data = response.json()
    print(response_data["message"])

    assert response_data["responseCode"] == 405
    assert response_data["message"] == "This request method is not supported."
