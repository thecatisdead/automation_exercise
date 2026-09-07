import pytest

from playwright.sync_api import Page

from pages.login_user_page import LoginPage
from pages.navbar_page import NavbarPage


@pytest.fixture
def launch_browser(page: Page):
    login_user_page = LoginPage(page)

    navbar_page = NavbarPage(page)
    navbar_page.navigate()

    login_user_page.verify_on_homepage()

    return login_user_page
