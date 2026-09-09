import pytest
from playwright.sync_api import Page
from pages.navbar_page import NavbarPage
from pages.products_page import AddProductsPage
from pages.register_user_page import RegistrationPage
from pages.login_user_page import LoginPage


def test_place_order_login_before_checkout(page: Page, setup_browser):
    login_user_page = setup_browser

    navbar_page = NavbarPage(page)
    products_page = AddProductsPage(page)
    register_user_page = RegistrationPage(page)

    navbar_page.go_to_login()
    login_user_page.login("junuelloginbefore@gmail.com", "password123")

    login_user_page.verify_logged_in_user()

    products_page.add_first_product_to_cart()

    products_page.view_cart_page()

    products_page.verify_view_cart_page()

    products_page.proceed_to_checkout()

    products_page.verify_delivery()
    products_page.verify_order()
    products_page.message_place_order()

    products_page.payment(
        name_on_card="junuel dizon",
        card_number="234234",
        cvc="344",
        expiry_month="July 10",
        expiry_year="2028",
    )

    # register_user_page.delete_account()

    # register_user_page.verify_account_deleted()

    # register_user_page.click_continue_button()
