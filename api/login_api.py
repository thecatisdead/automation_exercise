import requests


class LoginAPI:
    BASE_URL = "https://automationexercise.com/api"

    def post_login_valid_details(self, email_input: str, password_input: str):

        return requests.post(
            f"{self.BASE_URL}/verifyLogin",
            data={"email": email_input, "password": password_input},
        )

    def post_login_missing_param(self):
        return requests.post(f"{self.BASE_URL}/verifyLogin")

    def delete_login(self):
        return requests.delete(f"{self.BASE_URL}/verifyLogin")

    def post_login_invalid_details(self, email_input: str, password_input: str):
        return requests.post(
            f"{self.BASE_URL}/verifyLogin",
            data={"email": email_input, "password": password_input},
        )
