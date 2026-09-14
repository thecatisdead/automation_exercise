from playwright.sync_api import Page, expect


class ProductsPage:
    def __init__(self, page: Page):
        self.page = page

        self.view_first_product_link = page.locator('a[href="/product_details/1"]')
        self.products_name = page.locator("h2", has_text="Blue Top")
        self.products_category = page.get_by_text("Category: Women > Tops")
        self.products_price = page.get_by_text("Rs. 500")
        self.products_availability = page.get_by_text("Availability: In Stock")
        self.products_condition = page.get_by_text("Condition: New")
        self.products_brand = page.locator("p").filter(has_text="Brand: Polo")
        self.write_your_review = page.get_by_role("link", name="Write Your Review")
        self.brands = page.locator(".brands_products")
        self.kookie_kids_brand_link = page.get_by_role("link", name="Kookie Kids")
        self.polo_brand_link = page.get_by_role("link", name="Polo")
        self.kookie_brand_products_heading = page.get_by_role(
            "heading", name="Brand - Kookie Kids Products", exact=True
        )
        self.polo_brand_products_heading = page.get_by_role(
            "heading", name="Brand - Polo Products", exact=True
        )
        self.brand_products = page.locator(".features_items .product-image-wrapper")
        self.search_product_input = page.get_by_placeholder("Search Product")
        self.search_button = page.locator("#submit_search")
        self.searched_products_heading = page.get_by_role(
            "heading", name="Searched Products", level=2
        )
        self.search_blue_top = page.locator(".single-products").filter(
            has_text="Blue Top"
        )
        self.search_men_tshirt = page.locator(".single-products").filter(
            has_text="Men Tshirt"
        )

    def verify_write_your_review(self):
        expect(self.write_your_review).to_be_visible()

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

    def view_first_product_details(self):
        self.view_first_product_link.click()

    def search_product(self, product_name: str):
        self.search_product_input.fill(product_name)

    def verify_search_input_value(self, expected_value: str):
        expect(self.search_product_input).to_have_value(expected_value)

    def search_click_button(self):
        with self.page.expect_response(lambda response: "search" in response.url):
            self.search_button.click(force=True)

    def verify_searched_products_heading(self):
        expect(self.searched_products_heading).to_be_visible(timeout=15000)

    def verify_search_blue_top(self):
        expect(self.search_blue_top).to_be_visible()
        expect(self.search_blue_top.locator(".productinfo h2")).to_have_text("Rs. 500")
        expect(self.search_blue_top.locator(".productinfo p")).to_have_text("Blue Top")

    def verify_search_men_tshirt(self):
        expect(self.search_men_tshirt).to_be_visible()
        expect(self.search_men_tshirt.locator(".productinfo h2")).to_have_text(
            "Rs. 400"
        )
        expect(self.search_men_tshirt.locator(".productinfo p")).to_have_text(
            "Men Tshirt"
        )

    def verify_brands_left_sidebar(self):
        expect(self.brands).to_be_visible()

    def kookie_kids_brand(self):
        self.kookie_kids_brand_link.click()

    def verify_kookie_on_brand_products_page(self):
        expect(self.page).to_have_url(
            "https://automationexercise.com/brand_products/Kookie%20Kids"
        )

    def verify_kookie_brand_products_displayed(self):
        expect(self.kookie_brand_products_heading).to_be_visible()
        expect(self.brand_products).to_have_count(3)

    def polo_brand(self):
        self.polo_brand_link.click()

    def verify_polo_on_brand_products_page(self):
        expect(self.page).to_have_url(
            "https://automationexercise.com/brand_products/Polo"
        )

    def verify_polo_brand_products_displayed(self):
        expect(self.polo_brand_products_heading).to_be_visible()
        expect(self.brand_products).to_have_count(6)


class ProductReviewPage:
    def __init__(self, page: Page):
        self.page = page

        self.review_name_input = page.get_by_placeholder("Your Name")
        self.review_email_input = page.get_by_placeholder("Email Address", exact=True)
        self.review_textarea = page.get_by_placeholder("Add Review Here!")
        self.submit_review_button = page.get_by_role("button", name="Submit")
        self.review_success_message = page.get_by_text("Thank you for your review.")

    def fill_review_form(
        self, review_name: str, review_email: str, review_textarea: str
    ):
        self.submit_review_button.scroll_into_view_if_needed()
        self.review_name_input.fill(review_name)
        self.review_email_input.fill(review_email)
        self.review_textarea.fill(review_textarea)
        self.submit_review_button.click()

    def verify_review_success_message(self):
        expect(self.review_success_message).to_be_visible()
