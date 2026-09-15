import requests


class BrandsAPI:
    BASE_URL = "https://automationexercise.com/api"

    def get_all_brands(self):

        return requests.get(f"{self.BASE_URL}/brandsList")

    def put_brands_not_allowed(self):

        return requests.put(f"{self.BASE_URL}/brandsList")
