from playwright.sync_api import Page, expect


class SubscribePage:
    def __init__(self, page: Page):
        self.page = page

        self.footer = page.locator("#footer")

        self.subscription_text = page.locator("h2", has_text="Subscription")

        self.subscribe_email_input = page.locator("#susbscribe_email")

        self.subscribe_button = page.locator("#subscribe")

        self.subscription_success_message = page.get_by_text(
            "You have been successfully subscribed!"
        )

    def scroll_to_footer(self):
        self.footer.scroll_into_view_if_needed()

    def verify_subscription(self):
        expect(self.subscription_text).to_be_visible()

    def subscribe_email(self, subscribe_email: str):
        self.subscribe_email_input.fill(subscribe_email)
        self.subscribe_button.click()

    def verify_subscription_success(self):
        expect(self.subscription_success_message).to_be_visible()
