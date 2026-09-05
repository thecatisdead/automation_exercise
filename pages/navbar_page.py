from playwright.sync_api import Page, expect


class NavbarPage:
    def __init__(self, page: Page):
        self.page = page

        self.register_signup_link = page.get_by_role("link", name="Signup / Login")

        self.test_case_link = page.locator(".nav.navbar-nav a", has_text="Test Cases")

        self.test_cases_heading = page.locator("h2", has_text="Test Cases")

        self.products_link = page.get_by_role("link", name="Products")

        self.products_heading = page.locator("h2", has_text="Products")

        self.view_first_product_link = page.locator('a[href="/product_details/1"]')

        self.products_name = page.locator("h2", has_text="Blue Top")

        self.products_category = page.get_by_text("Category: Women > Tops")

        self.products_price = page.get_by_text("Rs. 500")

        self.products_availability = page.get_by_text("In Stock")

        self.products_condition = page.get_by_text("New")

        self.products_brand = page.locator("p").filter(has_text="Brand:")

        self.search_product_input = page.get_by_placeholder("Search Product")
        self.search_button = page.locator("#submit_search")
        self.searched_products_heading = page.locator(
            "h2", has_text="Searched Products"
        )

    def go_to_signup(self):
        self.register_signup_link.click()

    def go_to_test_cases(self):
        self.test_case_link.click()

    def view_first_product_details(self):
        self.view_first_product_link.click()

    def verify_on_test_cases_page(self):
        expect(self.page).to_have_url("https://automationexercise.com/test_cases")
        expect(self.test_cases_heading).to_be_visible()
        expect(self.test_cases_heading).to_have_text("Test Cases")

    def go_to_products(self):
        self.products_link.click()

    def verify_on_products_page(self):
        expect(self.page).to_have_url("https://automationexercise.com/products")
        expect(self.products_link).to_be_visible()
        expect(self.products_heading).to_have_text("All Products")

    def verify_on_product_details_page(self):
        expect(self.page).to_have_url(
            "https://automationexercise.com/product_details/1"
        )
        expect(self.products_name).to_be_visible()
        expect(self.products_category).to_be_visible()
        expect(self.products_price).to_be_visible()
        expect(self.products_availability).to_be_visible()
        expect(self.products_condition).to_be_visible()
        expect(self.products_brand).to_have_text("Brand: Polo")

    def search_product_input(self, product_name: str):
        self.search_product_input.fill(product_name)
        self.search_button.click()
        expect(self.searched_products_heading).to_be_visible()
