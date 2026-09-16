import pytest
import json
from api.search_products_api import SearchProductsAPI

# =========================================================================
# API 5: POST TO SEARCH PRODUCT
# =========================================================================


@pytest.fixture
def search_products_api():
    return SearchProductsAPI()


def test_search_product(search_products_api):
    response = search_products_api.post_search_products("Top")

    assert response.status_code == 200

    response_data = response.json()
    assert "products" in response_data
    assert len(response_data["products"]) > 0

    for product in response_data["products"]:
        assert (
            "top" in product["name"].lower()
            or "top" in product["category"]["category"].lower()
        )


# =========================================================================
# API 6: POST TO SEARCH PRODUCT WITHOUT SEARCH PRODUCT PARAMETER
# =========================================================================


def test_search_product_missing_param(search_products_api):
    response = search_products_api.post_search_product_missing_param()

    response_data = response.json()
    assert response_data["responseCode"] == 400
    assert (
        response_data["message"]
        == "Bad request, search_product parameter is missing in POST request."
    )
