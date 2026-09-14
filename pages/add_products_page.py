from playwright.sync_api import Page, expect


class AddProductsPage:
    def __init__(self, page: Page):
        self.page = page

        self.first_product = (
            page.locator(".product-image-wrapper")
            .filter(has=page.locator('[data-product-id="1"]'))
            .first
        )
        self.second_product = (
            page.locator(".product-image-wrapper")
            .filter(has=page.locator('[data-product-id="2"]'))
            .first
        )
        self.continue_shopping_button = page.get_by_role(
            "button", name="Continue Shopping"
        )
        self.view_cart_link = page.get_by_role("link", name="View Cart")
        self.first_product_in_cart = page.locator("#product-1")
        self.second_product_in_cart = page.locator("#product-2")
        self.third_product_link = page.locator('a[href="/product_details/3"]')
        self.third_product_in_cart = page.locator("#product-3")
        self.product_quantity_input = page.locator("#quantity")
        self.add_to_cart_button = page.get_by_role("button", name="Add to cart")
        self.recommended_items = page.locator(".recommended_items")
        self.first_recommended_item_link = self.recommended_items.locator(
            '.productinfo [data-product-id="4"].add-to-cart'
        )

    def add_first_product_to_cart(self):
        self.first_product.hover()
        overlay_button = self.first_product.locator(
            '.product-overlay [data-product-id="1"]'
        )
        overlay_button.wait_for(state="visible", timeout=5000)
        overlay_button.click()

    def continue_shopping(self):
        self.continue_shopping_button.click()

    def add_second_product_to_cart(self):
        self.second_product.hover()
        overlay_button = self.second_product.locator(
            '.product-overlay [data-product-id="2"]'
        )
        overlay_button.wait_for(state="visible", timeout=5000)
        overlay_button.click()

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
        for _ in range(amount):
            self.product_quantity_input.press("ArrowUp")
        self.product_quantity_input.press("Tab")

    def add_to_cart(self):
        with self.page.expect_response(
            lambda response: "cart" in response.url
        ) as response_info:
            self.add_to_cart_button.click()
        print("Add to cart response status:", response_info.value.status)

    def view_cart_page(self):
        self.view_cart_link.click()

    def verify_products_quantity_in_cart(self):
        expect(
            self.third_product_in_cart.locator(".cart_quantity button")
        ).to_have_text("4")

    def add_first_recommended_item_to_cart(self):
        self.first_recommended_item_link.click()
