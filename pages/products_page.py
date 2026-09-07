from playwright.sync_api import Page, expect


class ProductsPage:
    def __init__(self, page: Page):
        self.page = page

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

    def search_product(self, product_name: str):
        self.search_product_input.fill(product_name)
        self.search_button.click()
        expect(self.searched_products_heading).to_be_visible()

    def view_first_product_details(self):
        self.view_first_product_link.click()


class AddProductsPage:
    def __init__(self, page: Page):
        self.page = page

        self.first_product = page.locator(".product-image-wrapper").filter(
            has=page.locator('[data-product-id="1"]')
        )

        self.second_product = page.locator(".product-image-wrapper").filter(
            has=page.locator('[data-product-id="2"]')
        )

        self.continue_shopping_button = page.get_by_role(
            "button", name="Continue Shopping"
        )

        self.view_cart = page.get_by_role("link", name="View Cart")

        self.first_product_in_cart = page.locator("#product-1")

        self.second_product_in_cart = page.locator("#product-2")

        self.third_product_link = page.locator('a[href="/product_details/3"]')

        self.product_quantity_input = page.locator("#quantity")

        self.add_to_cart_button = page.get_by_role("button", name="Add to cart")

        self.verify_product_displayed_cart = page.locator(
            ".cart_quantity button", has_text="4"
        )

    def add_first_product_to_cart(self):
        self.first_product.hover()

        self.first_product.locator('.product-overlay [data-product-id="1"]').click()
        self.continue_shopping_button.click()

    def add_second_product_to_cart(self):
        self.second_product.hover()

        self.second_product.locator('.product-overlay [data-product-id="2"]').click()

    def view_cart_page(self):
        self.view_cart.click()

    def verify_both_products_in_cart(self):
        expect(self.first_product_in_cart).to_be_visible()
        expect(self.second_product_in_cart).to_be_visible()

    def verify_first_product_details(self):
        expect(self.first_product_in_cart.locator(".cart_price p")).to_have_text(
            "Rs. 500"
        )
        expect(
            self.first_product_in_cart.locator(".cart_quantity button")
        ).to_have_text("1")
        expect(self.first_product_in_cart.locator(".cart_total p")).to_have_text(
            "Rs. 500"
        )

    def verify_second_product_details(self):
        expect(self.second_product_in_cart.locator(".cart_price p")).to_have_text(
            "Rs. 400"
        )
        expect(
            self.second_product_in_cart.locator(".cart_quantity button")
        ).to_have_text("1")
        expect(self.second_product_in_cart.locator(".cart_total p")).to_have_text(
            "Rs. 400"
        )

    def view_third_product_details(self):
        self.third_product_link.click()

    def verify_product_detail_page(self):
        expect(self.page).to_have_url(
            "https://automationexercise.com/product_details/3"
        )

    def increase_quantity(self, amount: int):

        for i in range(amount):
            self.product_quantity_input.press("ArrowUp")

    def add_to_cart(self):
        self.add_to_cart_button.click()

    def verify_products_quantity_in_cart(self):
        expect(self.verify_product_displayed_cart).to_be_visible()
