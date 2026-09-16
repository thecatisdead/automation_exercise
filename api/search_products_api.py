import requests


class SearchProductsAPI:
    BASE_URL = "https://automationexercise.com/api"

    def post_search_products(self, search_term: str):

        return requests.post(
            f"{self.BASE_URL}/searchProduct",
            data={"search_product": search_term},
        )

    def post_search_product_missing_param(self):

        return requests.post(
            f"{self.BASE_URL}/searchProduct",
        )
