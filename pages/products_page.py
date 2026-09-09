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

        self.view_cart = page.get_by_role("link", name="View Cart")

        self.first_product_in_cart = page.locator("#product-1")

        self.second_product_in_cart = page.locator("#product-2")

        self.third_product_link = page.locator('a[href="/product_details/3"]')

        self.product_quantity_input = page.locator("#quantity")

        self.add_to_cart_button = page.get_by_role("button", name="Add to cart")

        self.verify_product_displayed_cart = page.locator(
            ".cart_quantity button", has_text="4"
        )

        self.proceed_to_checkout_button = page.locator("a.check_out")
        self.register_login_link = page.get_by_role("link", name="Register / Login")

        self.verify_delivery_address = page.locator("#address_delivery")

        self.verify_order_review = page.locator("table.table.table-condensed")

        self.enter_description_message = page.locator('textarea[name="message"]')

        self.place_order_button = page.get_by_role("link", name="Place Order")

        self.name_on_card_input = page.locator('[data-qa="name-on-card"]')

        self.card_number_input = page.locator('[data-qa="card-number"]')

        self.cvc_input = page.locator('[data-qa="cvc"]')

        self.expiry_month_input = page.locator('[data-qa="expiry-month"]')

        self.expiry_year_input = page.locator('[data-qa="expiry-year"]')

        self.pay_button = page.locator('[data-qa="pay-button"]')

        self.remove_product_button = page.locator('[data-product-id="1"]')

        self.cart_empty = page.get_by_text("Cart is empty!")

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

    def add_first_product_to_cart(self):
        self.first_product.hover()

        self.first_product.locator('.product-overlay [data-product-id="1"]').click()

    def continue_shopping(self):
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

    def verify_view_cart_page(self):
        expect(self.page).to_have_url("https://automationexercise.com/view_cart")

    def proceed_to_checkout(self):
        self.page.wait_for_timeout(1000)
        self.proceed_to_checkout_button.click()
        self.page.wait_for_url("**/checkout**", timeout=10000)

    def register_login(self):
        self.register_login_link.click()

    def verify_delivery(self):
        expect(self.verify_delivery_address).to_contain_text("Mr. junuel dizon")
        expect(self.verify_delivery_address).to_contain_text("ABC Company")
        expect(self.verify_delivery_address).to_contain_text("123 Main St")
        expect(self.verify_delivery_address).to_contain_text("Apt 4B")
        expect(self.verify_delivery_address).to_contain_text("New York NY 10001")
        expect(self.verify_delivery_address).to_contain_text("United States")
        expect(self.verify_delivery_address).to_contain_text("0912345678")

    def verify_order(self):
        expect(self.verify_order_review).to_contain_text("Blue Top")
        # expect(self.verify_order_review).to_contain_text("1")
        expect(self.verify_order_review).to_contain_text("Rs. 500")

    def message_place_order(self):
        self.enter_description_message.fill("Please deliver carefully.")
        self.place_order_button.click()

    def payment(
        self,
        name_on_card: str,
        card_number: str,
        cvc: str,
        expiry_month: str,
        expiry_year: str,
    ):
        self.name_on_card_input.fill(name_on_card)
        self.card_number_input.fill(card_number)
        self.cvc_input.fill(cvc)
        self.expiry_month_input.fill(expiry_month)
        self.expiry_year_input.fill(expiry_year)
        self.pay_button.click()

    def remove_product(self):
        self.remove_product_button.click()

    def verify_product_is_removed(self):
        expect(self.cart_empty).to_be_visible()

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

    def open_men_category(self):
        self.men_category.wait_for(state="visible")
        self.page.wait_for_timeout(1000)
        self.men_category.click()
        self.men_panel.wait_for(state="visible", timeout=10000)

    def verify_men_category_expanded(self):
        expect(self.men_panel).to_be_visible()

    def category_tshirts(self):
        self.category_tshirts_link.click()

    def verify_women_dress_heading(self):
        expect(self.page).to_have_url(
            "https://automationexercise.com/category_products/1"
        )
        expect(self.women_dress_products_heading).to_be_visible()

    def verify_men_tshirts_heading(self):
        expect(self.page).to_have_url(
            "https://automationexercise.com/category_products/3"
        )
        expect(self.men_tshirts_products_heading).to_be_visible()
