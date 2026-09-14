from playwright.sync_api import Page, expect


class NavbarPage:
    def __init__(self, page: Page):
        self.page = page

        self.nav_login_signup_link = page.locator(".nav.navbar-nav a[href='/login']")
        self.nav_test_case_link = page.locator(".nav.navbar-nav a[href='/test_cases']")
        self.nav_products_link = page.locator(".nav.navbar-nav a[href='/products']")
        self.nav_cart_link = page.locator(".nav.navbar-nav a[href='/view_cart']")
        self.nav_logout_user_link = page.locator(".nav.navbar-nav a[href='/logout']")
        self.nav_contact_us_link = page.locator(".nav.navbar-nav a[href='/contact_us']")
        self.register_login_link = page.get_by_role("link", name="Register / Login")
        self.test_cases_heading = page.locator("h2", has_text="Test Cases")
        self.products_heading = page.locator("h2", has_text="Products")
        self.login_heading = page.get_by_role("heading", name="Login to your account")

    def navigate(self):
        self.page.goto("https://automationexercise.com/")

    def go_to_login_signup(self):
        self.nav_login_signup_link.click()

    def go_to_test_cases(self):
        self.nav_test_case_link.click()

    def go_to_contact(self):
        self.nav_contact_us_link.click()

    def go_to_cart(self):
        self.nav_cart_link.click()

    def go_to_products(self):
        self.nav_products_link.click()

    def logout_user(self):
        self.nav_logout_user_link.click()

    def register_login(self):
        self.register_login_link.click()

    def verify_on_test_cases_page(self):
        expect(self.page).to_have_url("https://automationexercise.com/test_cases")
        expect(self.test_cases_heading).to_be_visible()
        expect(self.test_cases_heading).to_have_text("Test Cases")

    def verify_on_products_page(self):
        expect(self.page).to_have_url("https://automationexercise.com/products")
        expect(self.nav_products_link).to_be_visible()
        expect(self.products_heading).to_have_text("All Products")

    def verify_contact_us_form(self):
        expect(self.page).to_have_url("https://automationexercise.com/contact_us")
        expect(self.nav_contact_us_link).to_be_visible()

    def verify_login_page(self):
        expect(self.page).to_have_url("https://automationexercise.com/login")
        expect(self.login_heading).to_be_visible()
        expect(self.login_heading).to_have_text("Login to your account")
