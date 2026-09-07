from playwright.sync_api import Page, expect


class RegistrationPage:
    def __init__(self, page: Page):
        self.page = page

        self.title_heading = page.locator("#slider-carousel .item.active h1")

        self.register_heading = page.get_by_role("heading", name="New User Signup!")

        self.register_enter_account_info_heading = page.get_by_role(
            "heading", name="Enter Account Information"
        )

        self.register_name_input = page.locator("[data-qa='signup-name']")

        self.register_email_input = page.locator("[data-qa='signup-email']")

        self.register_button = page.locator("[data-qa='signup-button']")

        self.signup_error_message = page.get_by_text("Email Address already exist!")

        # ========================================================================
        # Enter Account Information
        # ========================================================================
        self.male_radio = page.locator("#id_gender1")

        self.female_radio = page.locator("#id_gender2")

        self.password_input = page.locator("[data-qa='password']")

        self.day_select = page.locator("[data-qa='days']")
        self.month_select = page.locator("[data-qa='months']")
        self.year_select = page.locator("[data-qa='years']")

        self.offers_checkbox = page.locator("#optin")
        self.newsletter_checkbox = page.locator("#newsletter")

        # ========================================================================
        # Address Information
        # ========================================================================

        self.register_firstname_input = page.locator("[data-qa='first_name']")
        self.register_lastname_input = page.locator("[data-qa='last_name']")
        self.register_company_input = page.locator("[data-qa='company']")
        self.register_address1_input = page.locator("[data-qa='address']")
        self.register_address2_input = page.locator("[data-qa='address2']")
        self.register_country_select = page.locator("[data-qa='country']")
        self.register_city_input = page.locator("[data-qa='city']")
        self.register_state_input = page.locator("[data-qa='state']")
        self.register_zipcode_input = page.locator("[data-qa='zipcode']")
        self.register_mobile_number_input = page.locator("[data-qa='mobile_number']")
        self.register_create_account_button = page.locator("[data-qa='create-account']")
        self.register_succeful_message = page.locator("[data-qa='account-created']")
        self.continue_button = page.locator("[data-qa='continue-button']")

        # =======================================================================
        # Delete Account
        # ========================================================================

        self.delete_account_button = page.get_by_role("link", name="Delete Account")
        self.account_delete_succeful_message = page.locator(
            "[data-qa='account-deleted']"
        )

    # def navigate(self):
    #     self.page.goto("https://automationexercise.com")

    # def verify_on_homepage(self):
    #     expect(self.page).to_have_url("https://automationexercise.com/")
    #     expect(self.title_heading).to_be_visible()
    #     expect(self.title_heading).to_have_text("AutomationExercise")

    def verify_new_user_signup(self):
        expect(self.page).to_have_url("https://automationexercise.com/login")
        expect(self.register_heading).to_be_visible()
        expect(self.register_heading).to_have_text("New User Signup!")

    def verify_enter_account_info(self):
        expect(self.page).to_have_url("https://automationexercise.com/signup")
        expect(self.register_enter_account_info_heading).to_be_visible()
        expect(self.register_enter_account_info_heading).to_have_text(
            "Enter Account Information"
        )

    def verify_account_deleted(self):
        expect(self.page).to_have_url("https://automationexercise.com/delete_account")
        expect(self.account_delete_succeful_message).to_be_visible()
        expect(self.account_delete_succeful_message).to_have_text("Account Deleted!")

    def verify_account_created(self):
        expect(self.page).to_have_url("https://automationexercise.com/account_created")
        expect(self.register_succeful_message).to_be_visible()
        expect(self.register_succeful_message).to_have_text("Account Created!")

    def verify_signup_error(self):
        expect(self.signup_error_message).to_be_visible()
        expect(self.signup_error_message).to_have_text("Email Address already exist!")

    def signup(self, name: str, email: str):
        self.register_name_input.fill(name)
        self.register_email_input.fill(email)
        self.register_button.click()

    def select_male(self):
        self.male_radio.check()

    def select_female(self):
        self.female_radio.check()

    def enter_password(self, password: str):
        self.password_input.fill(password)

    def select_day(self, day: str, month: str, year: str):
        self.day_select.select_option(day)
        self.month_select.select_option(month)
        self.year_select.select_option(year)

    def select_newsletter(self):
        self.newsletter_checkbox.check()

    def select_special_offers(self):
        self.offers_checkbox.check()

    def enter_address_info(
        self,
        first_name: str,
        last_name: str,
        company: str,
        address1: str,
        address2: str,
        country: str,
        city: str,
        state: str,
        zipcode: str,
        mobile_number: str,
    ):
        self.register_firstname_input.fill(first_name)
        self.register_lastname_input.fill(last_name)
        self.register_company_input.fill(company)
        self.register_address1_input.fill(address1)
        self.register_address2_input.fill(address2)
        self.register_country_select.select_option(country)
        self.register_city_input.fill(city)
        self.register_state_input.fill(state)
        self.register_zipcode_input.fill(zipcode)
        self.register_mobile_number_input.fill(mobile_number)
        self.register_create_account_button.click()

    def click_continue_button(self):
        self.continue_button.click()

    def delete_account(self):
        self.delete_account_button.click()
