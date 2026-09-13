import pytest
from playwright.sync_api import Page, expect

from pages.navbar_page import NavbarPage
from pages.subscription_page import SubscribePage

# =========================================================================
# TEST CASE 10: VERIFY SUBSCRIPTION IN HOMEPAGE
# =========================================================================


# def test_verify_subscription_homepage(page: Page, setup_browser):
#     setup_browser
#     NavbarPage(page)
#     subscription_page = SubscribePage(page)

#     subscription_page.scroll_to_footer()
#     subscription_page.verify_subscription()

#     subscription_page.subscribe_email("johndoe@gmail.com")
#     subscription_page.verify_subscription_success()


# =========================================================================
# TEST CASE 11: VERIFY SUBSCRIPTION IN CARTPAGE
# =========================================================================


def test_verify_subscription_cartpage(page: Page, setup_browser):
    setup_browser
    navbar_page = NavbarPage(page)
    subscription_page = SubscribePage(page)

    navbar_page.go_to_cart()

    subscription_page.scroll_to_footer()
    subscription_page.verify_subscription()

    subscription_page.subscribe_email("johndoe@gmail.com")
    subscription_page.verify_subscription_success()
