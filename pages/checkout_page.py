from playwright.sync_api import Page, expect


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page

        self.verify_order_review = page.locator("table.table.table-condensed")
        self.enter_description_message = page.locator('textarea[name="message"]')
        self.place_order_button = page.get_by_role("link", name="Place Order")

    def verify_order(self):
        expect(self.verify_order_review).to_contain_text("Blue Top")
        # expect(self.verify_order_review).to_contain_text("1")
        expect(self.verify_order_review).to_contain_text("Rs. 500")

    def message_place_order(self):
        self.enter_description_message.fill("Please deliver carefully.")
        self.place_order_button.click()
