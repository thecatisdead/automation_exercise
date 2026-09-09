import pytest
from playwright.sync_api import Page
from pages.navbar_page import NavbarPage
from pages.products_page import ProductsPage
from pages.products_page import AddProductsPage

# =========================================================================
# TEST CASE 8: VERIFY ALL PRODUCTS
# =========================================================================


def test_verify_products_details(page: Page, setup_browser):
    setup_browser

    navbar_page = NavbarPage(page)
    products_page = ProductsPage(page)

    navbar_page.go_to_products()

    navbar_page.verify_on_products_page()

    products_page.view_first_product_details()

    products_page.verify_on_product_details_page()


# =========================================================================
# TEST CASE 9: SEARCH PRODUCT
# =========================================================================


def test_search_product(page: Page, setup_browser):
    setup_browser

    navbar_page = NavbarPage(page)

    products_page = ProductsPage(page)

    products_page = AddProductsPage(page)

    navbar_page.go_to_products()

    navbar_page.verify_on_products_page()

    products_page.search_product("Men Tshirt")

    # expect(navbar_page.search_product_input).to_have_value("Men Tshirt")
