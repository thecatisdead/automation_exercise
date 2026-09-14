import pytest

from playwright.sync_api import Page


from pages.navbar_page import NavbarPage
from pages.subscription_page import SubscribePage
from pages.hompage_page import HomePage

# =========================================================================
# TEST CASE 25: VERIFY SCROLL UP WITH 'ARROW' AND SCROLL DOWN FUNCTIONALITY
# =========================================================================


def test_verify_scroll_up_and_down(page: Page, setup_browser):
    setup_browser

    NavbarPage(page)
    subscription_page = SubscribePage(page)
    homepage_page = HomePage(page)

    subscription_page.scroll_to_footer()
    subscription_page.verify_subscription()
    homepage_page.verify_scroll_up_button()
    homepage_page.verify_automation_engineer_text()


# =========================================================================
# TEST CASE 26: VERIFY SCROLL UP WITHOUT 'ARROW' & SCROLL DOWN FUNCTIONALITY
# =========================================================================


def test_verify_scroll_up_without_button_and_down(page: Page, setup_browser):
    setup_browser

    NavbarPage(page)
    subscription_page = SubscribePage(page)
    homepage_page = HomePage(page)

    subscription_page.scroll_to_footer()
    subscription_page.verify_subscription()
    homepage_page.scroll_to_header()
    homepage_page.verify_automation_engineer_text()
