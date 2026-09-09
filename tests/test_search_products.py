import pytest
import time


from playwright.sync_api import Page
from pages.navbar_page import NavbarPage
from pages.products_page import AddProductsPage
from pages.register_user_page import RegistrationPage
from pages.products_page import ProductsPage
from pages.login_user_page import LoginPage


def test_search_product_verify_cart_after_login(page: Page, setup_browser):
    setup_browser
    navbar_page = NavbarPage(page)

    products_page = ProductsPage(page)

    products_page = AddProductsPage(page)

    login_user_page = LoginPage(page)

    navbar_page.go_to_products()

    navbar_page.verify_on_products_page()

    products_page.search_product("Blue Top")

    products_page.search_click_button()

    # products_page.verify_searched_products_heading()

    products_page.verify_search_blue_top()

    products_page.add_first_product_to_cart()

    products_page.continue_shopping()

    products_page.search_product("Men Tshirt")

    products_page.search_click_button()

    products_page.verify_search_men_tshirt()

    products_page.add_second_product_to_cart()

    products_page.view_cart_page()

    products_page.verify_both_products_in_cart()

    login_user_page.go_to_login()

    login_user_page.verify_login_page()

    login_user_page.login("junueljonn@gmail.com", "password123")

    navbar_page.go_to_cart()

    products_page.verify_both_products_in_cart()
