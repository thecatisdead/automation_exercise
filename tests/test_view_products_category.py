import pytest
from playwright.sync_api import Page
from pages.navbar_page import NavbarPage
from pages.products_page import AddProductsPage
from pages.register_user_page import RegistrationPage


def test_place_order_register_while_checkout(page: Page, setup_browser):
    login_user_page = setup_browser

    navbar_page = NavbarPage(page)
    products_page = AddProductsPage(page)
    register_user_page = RegistrationPage(page)

    products_page.verify_categories_visible()
    products_page.open_women_category()
    products_page.verify_women_category_expanded()
    products_page.category_dress()
    products_page.verify_women_dress_heading()

    products_page.open_men_category()
    products_page.verify_men_category_expanded()
    products_page.category_tshirts()
    products_page.verify_men_tshirts_heading()
