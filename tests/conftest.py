import pytest

from playwright.sync_api import Page

from pages.login_user_page import LoginPage
from pages.navbar_page import NavbarPage
from pages.register_user_page import RegistrationPage
from pages.products_page import ProductsPage, AddProductsPage, ProductReviewPage
from pages.checkout_page import CheckoutPage
from pages.hompage_page import HomePage


@pytest.fixture
def setup_browser(page: Page):

    page.route("**/*doubleclick*", lambda route: route.abort())
    page.route("**/*googlesyndication*", lambda route: route.abort())
    page.route("**/*adservice*", lambda route: route.abort())
    page.route("**/*googletagmanager*", lambda route: route.abort())
    page.route("**/*google_vignette*", lambda route: route.abort())
    page.route("**/pagead2.googlesyndication.com/**", lambda route: route.abort())
    page.route("**/securepubads.g.doubleclick.net/**", lambda route: route.abort())
    page.route("**/*googleadservices*", lambda route: route.abort())

    homepage_page = HomePage(page)

    navbar_page = NavbarPage(page)
    navbar_page.navigate()

    homepage_page.verify_on_homepage()

    return homepage_page


@pytest.fixture
def user_info(page: Page):

    def fill_user_info():
        register_user_page = RegistrationPage(page)

        register_user_page.male_radio.check()
        register_user_page.enter_password("password123")

        register_user_page.select_day("2", "10", "2000")

        register_user_page.select_newsletter()
        register_user_page.select_special_offers()

        register_user_page.enter_address_info(
            first_name="junuel",
            last_name="dizon",
            company="ABC Company",
            address1="123 Main St",
            address2="Apt 4B",
            country="United States",
            city="New York",
            state="NY",
            zipcode="10001",
            mobile_number="0912345678",
        )

        register_user_page.verify_account_created()
        register_user_page.click_continue_button()

    return fill_user_info


@pytest.fixture
def delivery_address(page: Page):

    def fill_delivery_address_info():

        products_page = ProductsPage(page)
        checkout_page = CheckoutPage(page)
        products_page = ProductReviewPage(page)
        products_page = AddProductsPage(page)

        products_page.proceed_to_checkout()

        checkout_page.verify_delivery_address(
            name="junuel dizon",
            company="ABC Company",
            address1="123 Main St",
            address2="Apt 4B",
            city="New York",
            state="NY",
            zipcode="10001",
            country="United States",
            mobile_number="0912345678",
        )

        products_page.verify_order()

        products_page.message_place_order()

    return fill_delivery_address_info


@pytest.fixture
def card_info(page: Page):

    def fill_card_info():

        checkout_page = CheckoutPage(page)

        checkout_page.payment(
            name_on_card="junuel dizon",
            card_number="234234",
            cvc="344",
            expiry_month="July 10",
            expiry_year="2028",
        )

    return fill_card_info


@pytest.fixture
def delete_account(page: Page):
    def _delete_account():
        register_user_page = RegistrationPage(page)
        register_user_page.delete_account()
        register_user_page.verify_account_deleted()
        register_user_page.click_continue_button()

    return _delete_account
