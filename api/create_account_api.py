import requests


class CreateAPI:
    BASE_URL = "https://automationexercise.com/api"

    def post_create_account(
        self,
        name_input: str,
        email_input: str,
        password_input: str,
        title_input: str,
        birthdate_input: str,
        birthmonth_input: str,
        birthyear_input: str,
        firstname_input: str,
        lastname_input: str,
        company_input: str,
        address1_input: str,
        address2_input: str,
        country_input: str,
        zipcode_input: str,
        state_input: str,
        city_input: str,
        mobile_number_input: str,
    ):

        return requests.post(
            f"{self.BASE_URL}/createAccount",
            data={
                "name": name_input,
                "email": email_input,
                "password": password_input,
                "title": title_input,
                "birth_date": birthdate_input,
                "birth_month": birthmonth_input,
                "birth_year": birthyear_input,
                "firstname": firstname_input,
                "lastname": lastname_input,
                "company": company_input,
                "address1": address1_input,
                "address2": address2_input,
                "country": country_input,
                "zipcode": zipcode_input,
                "state": state_input,
                "city": city_input,
                "mobile_number": mobile_number_input,
            },
        )


class DeleteAPI:
    BASE_URL = "https://automationexercise.com/api"

    def delete_created_account(self, email_input: str, password_input: str):
        return requests.delete(
            f"{self.BASE_URL}/deleteAccount",
            data={"email": email_input, "password": password_input},
        )
