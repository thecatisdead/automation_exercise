import pytest
from playwright.sync_api import Page

from pages.navbar_page import NavbarPage
from pages.add_products_page import AddProductsPage

# =========================================================================
# TEST CASE 12: ADD PRODUCTS IN CART
# =========================================================================


def test_add_products_cart(page: Page, setup_browser):
    setup_browser
    navbar_page = NavbarPage(page)
    add_products_page = AddProductsPage(page)

    navbar_page.go_to_products()
    add_products_page.add_first_product_to_cart()
    add_products_page.continue_shopping()
    add_products_page.add_second_product_to_cart()
    add_products_page.view_cart_page()
    add_products_page.verify_both_products_in_cart()
    add_products_page.verify_first_product_details()
    add_products_page.verify_second_product_details()


# =========================================================================
# TEST CASE 13: VERIFY PRODUCT QUANTITY IN CART
# =========================================================================


def test_verify_product_quantity_in_cart(page: Page, setup_browser):
    setup_browser
    NavbarPage(page)
    add_products_page = AddProductsPage(page)

    add_products_page.view_third_product_details()
    add_products_page.verify_product_detail_page()
    add_products_page.increase_quantity(3)
    add_products_page.add_to_cart()
    add_products_page.view_cart_page()
    add_products_page.verify_products_quantity_in_cart()
