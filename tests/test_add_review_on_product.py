import pytest
from playwright.sync_api import Page
from pages.navbar_page import NavbarPage
from pages.products_page import ProductsPage
from pages.products_page import ProductReviewPage


def test_add_review_on_product(page: Page, setup_browser):
    setup_browser

    navbar_page = NavbarPage(page)
    products_page = ProductsPage(page)

    navbar_page.go_to_products()

    navbar_page.verify_on_products_page()

    products_page.view_first_product_details()

    products_page.verify_write_your_review()

    products_page = ProductReviewPage(page)

    products_page.fill_review_form(
        review_name="Junuel",
        review_email="junueldizon@gmail.com",
        review_textarea="I like this product",
    )

    products_page.verify_review_success_message()
