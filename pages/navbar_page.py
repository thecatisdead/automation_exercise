from playwright.sync_api import Page, expect


class NavbarPage:
    def __init__(self, page: Page):
        self.page = page

        self.nav_signup_link = page.get_by_role("link", name="Signup / Login")

        self.nav_login_link = page.get_by_role("link", name="Signup / Login")

        self.nav_test_case_link = page.locator(
            ".nav.navbar-nav a", has_text="Test Cases"
        )
        # self.nav_contact_us_link = page.get_by_role("link", name="Contact us")

        self.nav_cart_link = page.get_by_role("link", name="Cart", exact=True)

        self.nav_products_link = page.get_by_role("link", name="Products")

        # =======================================================================================

        self.test_cases_heading = page.locator("h2", has_text="Test Cases")

        self.products_heading = page.locator("h2", has_text="Products")

        # ===================================================================================================

    def navigate(self):
        self.page.goto("https://automationexercise.com/")

    def go_to_login(self):
        self.nav_login_link.click()

    def go_to_signup(self):
        self.nav_signup_link.click()

    def go_to_test_cases(self):
        self.nav_test_case_link.click()

    # def go_to_contact(self):
    #     self.nav_contact_us_link.click()

    def go_to_cart(self):
        self.nav_cart_link.click()

    def go_to_products(self):
        self.nav_products_link.click()

    def verify_on_test_cases_page(self):
        expect(self.page).to_have_url("https://automationexercise.com/test_cases")
        expect(self.test_cases_heading).to_be_visible()
        expect(self.test_cases_heading).to_have_text("Test Cases")

    def verify_on_products_page(self):
        expect(self.page).to_have_url("https://automationexercise.com/products")
        expect(self.nav_products_link).to_be_visible()
        expect(self.products_heading).to_have_text("All Products")
