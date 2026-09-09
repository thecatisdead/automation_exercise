import pytest
from playwright.sync_api import Page
from pages.navbar_page import NavbarPage
from pages.products_page import AddProductsPage
from pages.register_user_page import RegistrationPage


def test_remove_products_from_cart(page: Page, setup_browser):
    setup_browser

    navbar_page = NavbarPage(page)
    products_page = AddProductsPage(page)

    products_page.add_first_product_to_cart()
    products_page.view_cart_page()
    products_page.verify_view_cart_page()
    products_page.remove_product()
    products_page.verify_product_is_removed()
