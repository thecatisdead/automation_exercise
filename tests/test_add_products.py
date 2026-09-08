import pytest
from playwright.sync_api import Page, expect

from pages.navbar_page import NavbarPage
from pages.products_page import AddProductsPage

# =========================================================================
# TEST CASE 12: ADD PRODUCTS IN CART
# =========================================================================


def test_add_products_cart(page: Page, setup_browser):
    login_user_page = setup_browser
    navbar_page = NavbarPage(page)
    products_page = AddProductsPage(page)

    navbar_page.go_to_products()

    products_page.add_first_product_to_cart()
    products_page.continue_shopping()

    products_page.add_second_product_to_cart()
    products_page.view_cart_page()

    products_page.verify_both_products_in_cart()

    products_page.verify_first_product_details()

    products_page.verify_second_product_details()


# =========================================================================
# TEST CASE 13: VERIFY PRODUCT QUANTITY IN CART
# =========================================================================


def test_verify_product_quantity_in_cart(page: Page, setup_browser):
    login_user_page = setup_browser
    navbar_page = NavbarPage(page)
    products_page = AddProductsPage(page)

    products_page.view_third_product_details()
    products_page.verify_product_detail_page()
    products_page.increase_quantity(3)
    products_page.add_to_cart()
    products_page.view_cart_page()
    products_page.verify_products_quantity_in_cart()

    # page.pause()
