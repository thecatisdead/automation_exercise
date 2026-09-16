import pytest
import json
from api.products_api import ProductsAPI

# =========================================================================
# API 1: GET ALL PRODUCTS LIST
# =========================================================================


@pytest.fixture
def products_api():
    return ProductsAPI()


def test_get_all_products_list(products_api):
    response = products_api.get_all_products()

    response_data = response.json()
    assert response_data["responseCode"] == 200

    assert "products" in response_data
    assert isinstance(response_data["products"], list)
    assert len(response_data["products"]) > 0

    for product in response_data["products"]:
        assert "id" in product
        assert "name" in product
        assert "price" in product
        assert "brand" in product

    assert "category" in product
    print(json.dumps(response_data["products"], indent=4))


# =========================================================================
# API 2: POST TO ALL PRODUCTS LIST
# =========================================================================


def test_post_to_products_list_not_allowed(products_api):
    response = products_api.get_all_products_wrong_method()

    response_data = response.json()

    assert response_data["responseCode"] == 405
    assert response_data["message"] == "This request method is not supported."
