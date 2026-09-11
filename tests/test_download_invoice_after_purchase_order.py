import pytest
from pathlib import Path

from playwright.sync_api import Page

from pages.navbar_page import NavbarPage
from pages.products_page import AddProductsPage
from pages.register_user_page import RegistrationPage
from pages.login_user_page import LoginPage
from pages.checkout_page import CheckoutPage
from pages.navbar_page import NavbarPage

# =========================================================================
# TEST CASE 25:
# =========================================================================


def test_download_invoice_after_purchase_order(page: Page, setup_browser):
    setup_browser
    products_page = AddProductsPage(page)
    checkout_page = CheckoutPage(page)

    login_user_page = LoginPage(page)
    navbar_page = NavbarPage(page)
    products_page.add_first_product_to_cart()
    products_page.view_cart_page()
    products_page.verify_view_cart_page()

    products_page.proceed_to_checkout_no_account()

    register_user_page = RegistrationPage(page)

    products_page.register_login()

    # register_user_page.verify_new_user_signup()
    register_user_page.signup("junuel", "junueldownloadinvoice30@gmail.com")

    register_user_page.verify_enter_account_info()

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

    login_user_page.verify_logged_in_user()

    navbar_page.go_to_cart()

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

    products_page.payment(
        name_on_card="junuel dizon",
        card_number="234234",
        cvc="344",
        expiry_month="July 10",
        expiry_year="2028",
    )

    download = checkout_page.download_invoice()

    file_path = Path("invoice.txt")
    download.save_as(file_path)

    assert file_path.exists()
    assert file_path.read_text() != ""

    register_user_page.delete_account()

    register_user_page.verify_account_deleted()

    register_user_page.click_continue_button()
