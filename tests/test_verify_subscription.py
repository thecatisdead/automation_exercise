import pytest
from playwright.sync_api import Page, expect

from pages.navbar_page import NavbarPage
from pages.subscription_page import SubscribePage

# =========================================================================
# TEST CASE 10: VERIFY SUBSCRIPTION IN HOMEPAGE
# =========================================================================


def test_verify_subscription_homepage(page: Page, launch_browser):
    login_user_page = launch_browser
    navbar_page = NavbarPage(page)
    subscription_page = SubscribePage(page)

    subscription_page.scroll_to_footer()
    expect(subscription_page.footer).to_be_visible()
    subscription_page.verify_subscription()

    subscription_page.subscribe_email("johndoe@gmail.com")
    subscription_page.verify_subscription_success()


# =========================================================================
# TEST CASE 11: VERIFY SUBSCRIPTION IN CARTPAGE
# =========================================================================


def test_verify_subscription_cartpage(page: Page, launch_browser):
    login_user_page = launch_browser
    navbar_page = NavbarPage(page)
    subscription_page = SubscribePage(page)

    navbar_page.go_to_cart()

    subscription_page.scroll_to_footer()
    expect(subscription_page.footer).to_be_visible()
    subscription_page.verify_subscription()

    subscription_page.subscribe_email("johndoer@gmail.com")
    subscription_page.verify_subscription_success()


# page.pause()
