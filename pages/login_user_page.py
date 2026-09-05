from playwright.sync_api import Page, expect


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

        self.title_heading = page.locator("#slider-carousel .item.active h1")

        self.login_heading = page.get_by_role("heading", name="Login to your account")

        self.login_error_message = page.get_by_text(
            "Your email or password is incorrect!"
        )

        self.login_register_link = page.get_by_role("link", name="Signup / Login")

        self.login_email_input = page.locator("[data-qa='login-email']")

        self.login_password_input = page.locator("[data-qa='login-password']")

        self.login_button = page.locator("[data-qa='login-button']")

        self.logged_in_user = page.locator("a").filter(has_text="Logged in as")

        self.logout_user_link = page.get_by_role("link", name="Logout")

    def navigate(self):
        self.page.goto("https://automationexercise.com/")

    def verify_on_homepage(self):
        expect(self.page).to_have_url("https://automationexercise.com/")
        expect(self.title_heading).to_be_visible()
        expect(self.title_heading).to_have_text("AutomationExercise")

    def verify_login_page(self):
        expect(self.page).to_have_url("https://automationexercise.com/login")
        expect(self.login_heading).to_be_visible()
        expect(self.login_heading).to_have_text("Login to your account")

    def go_to_login(self):
        self.login_register_link.click()

    def login(self, email: str, password: str):
        self.login_email_input.fill(email)
        self.login_password_input.fill(password)
        self.login_button.click()

    def verify_logged_in_user(self):
        expect(self.logged_in_user).to_contain_text("Logged in as")
        expect(self.logged_in_user).to_contain_text("junuel")

    def verify_logged_in_user_incorrect(self):
        expect(self.login_error_message).to_be_visible()
        expect(self.login_error_message).to_have_text(
            "Your email or password is incorrect!"
        )

    def verify_contact_us_form(self):
        expect(self.page).to_have_url("https://automationexercise.com/contact_us")
        expect(self.contact_us_link).to_be_visible()
        expect(self.contact_us_link).to_have_text("Contact us")

    def logout_user(self):
        self.logout_user_link.click()
