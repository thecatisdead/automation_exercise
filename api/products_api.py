import requests


class ProductsAPI:
    BASE_URL = "https://automationexercise.com/api"

    def get_all_products(self):

        return requests.get(f"{self.BASE_URL}/productsList")

    def get_all_products_wrong_method(self):

        return requests.get(f"{self.BASE_URL}/productsList")
