import pytest
from playwright.sync_api import Page
from pages.navbar_page import NavbarPage
from pages.add_products_page import AddProductsPage
from pages.register_user_page import RegistrationPage
from pages.checkout_page import CheckoutPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.login_user_page import LoginPage


def test_place_order_register_while_checkout(
    page: Page, setup_browser, user_info, delivery_address, card_info, delete_account
):
    setup_browser

    login_user_page = LoginPage(page)
    navbar_page = NavbarPage(page)
    register_user_page = RegistrationPage(page)
    add_products_page = AddProductsPage(page)
    cart_page = CartPage(page)
    CheckoutPage(page)
    ProductsPage(page)

    add_products_page.add_first_product_to_cart()
    add_products_page.view_cart_page()
    cart_page.verify_view_cart_page()
    cart_page.proceed_to_checkout_no_account()
    navbar_page.register_login()
    register_user_page.signup("junuel", "junueljon147@gmail.com")
    user_info()
    login_user_page.verify_logged_in_user()
    navbar_page.go_to_cart()
    delivery_address()
    card_info()
    delete_account()
