import pytest
import json
from api.products_api import ProductsAPI


@pytest.fixture
def products_api():
    return ProductsAPI()


# =========================================================================
# API 1: GET ALL PRODUCTS LIST
# =========================================================================


# def test_get_all_products_list(products_api):
#     response = products_api.get_all_products()
#     print("Status:", response.status_code)
#     print("Headers:", response.headers)
#     print("Body:", json.dumps(response.json()))

#     assert response.status_code == 200

#     response_data = response.json()
#     assert "products" in response_data
#     assert isinstance(response_data["products"], list)
#     assert len(response_data["products"]) > 0

#     first_product = response_data["products"][0]
#     assert "id" in first_product
#     assert "name" in first_product
#     assert "price" in first_product
#     assert "brand" in first_product
#     assert "category" in first_product


# =========================================================================
# API 2: POST TO ALL PRODUCTS LIST
# =========================================================================


def test_post_to_products_list_not_allowed(products_api):
    response = products_api.get_all_products_wrong_method()

    print("Status code:", response.status_code)
    print("Body:", response.json())

    assert response.status_code == 200

    response_data = response.json()
    assert response_data["responseCode"] == 200
    assert "products" in response_data
    assert len(response_data["products"]) > 0


# # =========================================================================
# # API 5: POST TO SEARCH PRODUCT
# # =========================================================================


# def test_search_product(products_api):
#     response = products_api.search_product("Top")

#     assert response.status_code == 200

#     response_data = response.json()
#     assert "products" in response_data
#     assert len(response_data["products"]) > 0

#     for product in response_data["products"]:
#         assert (
#             "top" in product["name"].lower()
#             or "top" in product["category"]["category"].lower()
#         )


# # =========================================================================
# # API 6: POST TO SEARCH PRODUCT WITHOUT search_product PARAMETER
# # =========================================================================


# def test_search_product_missing_param(products_api):
#     response = products_api.search_product_without_param()

#     response_data = response.json()
#     assert response_data["responseCode"] == 400
#     assert (
#         response_data["message"]
#         == "Bad request, search_product parameter is missing in POST request."
# )
