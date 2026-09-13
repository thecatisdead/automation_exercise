import pytest
from playwright.sync_api import Page
from pages.navbar_page import NavbarPage
from pages.add_products_page import AddProductsPage
from pages.cart_page import CartPage


def test_remove_products_from_cart(page: Page, setup_browser):
    setup_browser

    NavbarPage(page)
    add_products_page = AddProductsPage(page)
    cart_page = CartPage(page)

    add_products_page.add_first_product_to_cart()
    add_products_page.view_cart_page()
    cart_page.verify_view_cart_page()
    cart_page.remove_product()
    cart_page.verify_product_is_removed()
