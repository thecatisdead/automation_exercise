import pytest
from playwright.sync_api import Page
from pages.navbar_page import NavbarPage
from pages.add_products_page import AddProductsPage
from pages.register_user_page import RegistrationPage
from pages.category_page import CategoryPage

# =========================================================================
# TEST CASE 18: VIEW CATEGORY PRODUCTS
# =========================================================================


def test_view_products_category(page: Page, setup_browser):
    setup_browser

    NavbarPage(page)
    category_page = CategoryPage(page)

    category_page.verify_categories_visible()
    category_page.open_women_category()
    category_page.verify_women_category_expanded()
    category_page.category_dress()
    category_page.verify_women_dress_heading()

    category_page.open_men_category()
    category_page.verify_men_category_expanded()
    category_page.category_tshirts()
    category_page.verify_men_tshirts_heading()
