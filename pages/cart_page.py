from playwright.sync_api import Page, expect


class CartPage:
    def __init__(self, page: Page):
        self.page = page

        self.recommended_items = page.locator(".recommended_items")
        self.cart_product_names = page.locator(".cart_description h4 a")
        self.remove_product_button = page.locator(
            '.cart_quantity_delete[data-product-id="1"]'
        )
        self.cart_empty = page.get_by_text("Cart is empty!")
        self.proceed_to_checkout_button = page.locator("a.check_out")

    def scroll_recommended_items(self):
        self.recommended_items.scroll_into_view_if_needed()

    def verify_recommended_item_in_cart(self, recommended_item: str):
        expect(
            self.cart_product_names.filter(has_text=recommended_item)
        ).to_be_visible()

    def verify_view_cart_page(self):
        expect(self.page).to_have_url("https://automationexercise.com/view_cart")

    def remove_product(self):
        self.remove_product_button.scroll_into_view_if_needed()
        self.remove_product_button.click(force=True)

    def verify_product_is_removed(self):
        expect(self.cart_empty).to_be_visible()

    def proceed_to_checkout(self):
        self.page.wait_for_timeout(1000)
        self.proceed_to_checkout_button.click()
        self.page.wait_for_url("**/checkout**", timeout=10000)

    def proceed_to_checkout_no_account(self):
        self.page.wait_for_timeout(1000)
        self.proceed_to_checkout_button.click()
