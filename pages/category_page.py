from playwright.sync_api import Page, expect


class CategoryPage:
    def __init__(self, page: Page):
        self.page = page

        self.categories = page.locator("#accordian")
        self.women_category = page.locator('a[href="#Women"]')
        self.women_panel = page.locator("#Women")
        self.category_dress_link = page.locator('a[href="/category_products/1"]')
        self.women_dress_products_heading = page.locator(
            "h2", has_text="Women - Dress Products"
        )
        self.men_category = page.locator('a[href="#Men"]')
        self.men_panel = page.locator("#Men")
        self.category_tshirts_link = page.locator('a[href="/category_products/3"]')
        self.men_tshirts_products_heading = page.locator(
            "h2", has_text="Men - Tshirts Products"
        )

    def verify_categories_visible(self):
        expect(self.categories).to_be_visible()

    def open_women_category(self):
        self.women_category.wait_for(state="visible")
        self.page.wait_for_timeout(1000)
        self.women_category.click()
        self.women_panel.wait_for(state="visible", timeout=10000)

    def verify_women_category_expanded(self):
        expect(self.women_panel).to_be_visible()

    def category_dress(self):
        self.category_dress_link.click()

    def verify_women_dress_heading(self):
        expect(self.page).to_have_url(
            "https://automationexercise.com/category_products/1"
        )
        expect(self.women_dress_products_heading).to_be_visible()

    def open_men_category(self):
        self.men_category.wait_for(state="visible")
        self.page.wait_for_timeout(1000)
        self.men_category.click()
        self.men_panel.wait_for(state="visible", timeout=10000)

    def verify_men_category_expanded(self):
        expect(self.men_panel).to_be_visible()

    def category_tshirts(self):
        self.category_tshirts_link.click()

    def verify_men_tshirts_heading(self):
        expect(self.page).to_have_url(
            "https://automationexercise.com/category_products/3"
        )
        expect(self.men_tshirts_products_heading).to_be_visible()
