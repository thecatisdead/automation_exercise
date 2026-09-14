import pytest
from pathlib import Path

from playwright.sync_api import Page

from pages.navbar_page import NavbarPage
from pages.add_products_page import AddProductsPage
from pages.register_user_page import RegistrationPage
from pages.login_user_page import LoginPage
from pages.checkout_page import CheckoutPage
from pages.navbar_page import NavbarPage
from pages.cart_page import CartPage
from pages.payment_page import PaymentPage

# =========================================================================
# TEST 24: DOWNLOAD INVOICE AFTER PURCHASE ORDER
# =========================================================================


def test_download_invoice_after_purchase_order(
    page: Page, setup_browser, user_info, delivery_address, card_info, delete_account
):
    setup_browser
    add_products_page = AddProductsPage(page)
    checkout_page = CheckoutPage(page)
    login_user_page = LoginPage(page)
    navbar_page = NavbarPage(page)
    add_products_page = AddProductsPage(page)
    cart_page = CartPage(page)
    payment_page = PaymentPage(page)

    add_products_page.add_first_product_to_cart()
    add_products_page.view_cart_page()
    cart_page.verify_view_cart_page()
    cart_page.proceed_to_checkout_no_account()
    register_user_page = RegistrationPage(page)
    navbar_page.register_login()
    register_user_page.verify_new_user_signup()
    register_user_page.signup("junuel", "junueldownloadinvoice43@gmail.com")
    user_info()
    login_user_page.verify_logged_in_user()
    navbar_page.go_to_cart()
    delivery_address()
    card_info()
    download = payment_page.download_invoice()
    file_path = Path("test.txt")
    download.save_as(file_path)

    assert file_path.exists()
    assert file_path.read_text() != ""

    delete_account()
