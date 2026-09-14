from playwright.sync_api import Page, expect


class HomePage:
    def __init__(self, page: Page):
        self.page = page

        self.scroll_up_button = page.locator("#scrollUp")
        self.title_heading = page.locator(
            "#slider-carousel .item.active h1", has_text="AutomationExercise"
        )
        self.header = page.locator("#header")
        self.verify_recommended_items_visibility = page.locator(".recommended_items")

    def verify_on_homepage(self):
        expect(self.page).to_have_url("https://automationexercise.com/", timeout=10000)
        expect(self.title_heading).to_be_visible()

    def verify_scroll_up_button(self):
        self.scroll_up_button.click()

    def scroll_to_header(self):
        self.header.scroll_into_view_if_needed()

    def verify_automation_engineer_text(self):

        expect(self.title_heading).to_be_in_viewport()
        self.title_heading.get_by_role(
            "heading",
            name="Full-Fledged practice website for Automation Engineers",
            exact=True,
        )

    def verify_recommended_items_are_visible(self):
        expect(self.verify_recommended_items_visibility).to_be_in_viewport()
        expect(self.verify_recommended_items_visibility).to_be_visible()
        expect(
            self.verify_recommended_items_visibility.get_by_role(
                "heading", name="recommended items", exact=True
            )
        ).to_be_visible()
