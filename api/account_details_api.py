import requests


class UserDetailsAPI:
    BASE_URL = "https://automationexercise.com/api"

    def get_user_details_by_email(self, email_input: str):

        return requests.get(
            f"{self.BASE_URL}/getUserDetailByEmail", params={"email": email_input}
        )
