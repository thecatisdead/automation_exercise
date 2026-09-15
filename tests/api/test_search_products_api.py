import pytest
import json
from api.search_products_api import SearchProductsAPI


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
