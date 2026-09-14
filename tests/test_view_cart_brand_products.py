import pytest
from playwright.sync_api import Page
from pages.navbar_page import NavbarPage
from pages.products_page import ProductsPage

# =========================================================================
# TEST CASE 19: VIEW & CART BRAND PRODUCTS
# =========================================================================


def test_view_cart_brand_products(page: Page, setup_browser):
    setup_browser

    navbar_page = NavbarPage(page)
    products_page = ProductsPage(page)

    navbar_page.go_to_products()

    products_page.verify_brands_left_sidebar()

    products_page.kookie_kids_brand()

    products_page.verify_kookie_on_brand_products_page()

    products_page.verify_kookie_brand_products_displayed()

    products_page.polo_brand()

    products_page.verify_polo_on_brand_products_page()

    products_page.verify_polo_brand_products_displayed()
