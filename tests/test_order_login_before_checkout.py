import pytest
from playwright.sync_api import Page
from pages.navbar_page import NavbarPage
from pages.register_user_page import RegistrationPage
from pages.login_user_page import LoginPage
from pages.checkout_page import CheckoutPage
from pages.hompage_page import HomePage
from pages.add_products_page import AddProductsPage
from pages.cart_page import CartPage


def test_place_order_login_before_checkout(
    page: Page, setup_browser, delivery_address, card_info, delete_account
):
    setup_browser

    navbar_page = NavbarPage(page)
    add_products_page = AddProductsPage(page)
    login_user_page = LoginPage(page)
    cart_page = CartPage(page)
    CheckoutPage(page)
    RegistrationPage(page)

    navbar_page.go_to_login_signup()
    login_user_page.login("junuelloginbefore6@gmail.com", "password123")

    login_user_page.verify_logged_in_user()

    add_products_page.add_first_product_to_cart()

    add_products_page.view_cart_page()

    cart_page.verify_view_cart_page()

    delivery_address()

    card_info()

    # delete_account()
