import pytest
from playwright.sync_api import Page, expect

from pages.navbar_page import NavbarPage
from pages.subscription_page import SubscribePage
from pages.cart_page import CartPage
from pages.add_products_page import AddProductsPage
from pages.hompage_page import HomePage

# =========================================================================
# TEST CASE 22: ADD TO CART FROM RECOMMENDED ITEMS
# =========================================================================


def test_add_to_cart_from_recommended_items(page: Page, setup_browser):
    setup_browser
    NavbarPage(page)
    cart_page = CartPage(page)
    add_products_page = AddProductsPage(page)
    homepage_page = HomePage(page)

    cart_page.scroll_recommended_items()

    homepage_page.verify_recommended_items_are_visible()

    add_products_page.add_first_recommended_item_to_cart()

    add_products_page.view_cart_page()

    cart_page.verify_recommended_item_in_cart("Stylish Dress")
