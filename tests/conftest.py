import pytest

from playwright.sync_api import Page

from pages.login_user_page import LoginPage
from pages.navbar_page import NavbarPage


@pytest.fixture
def setup_browser(page: Page):

    page.route("**/*doubleclick*", lambda route: route.abort())
    page.route("**/*googlesyndication*", lambda route: route.abort())
    page.route("**/*adservice*", lambda route: route.abort())
    page.route("**/*googletagmanager*", lambda route: route.abort())
    page.route("**/*google_vignette*", lambda route: route.abort())
    page.route("**/pagead2.googlesyndication.com/**", lambda route: route.abort())
    page.route("**/securepubads.g.doubleclick.net/**", lambda route: route.abort())
    page.route("**/*googleadservices*", lambda route: route.abort())

    login_user_page = LoginPage(page)

    navbar_page = NavbarPage(page)
    navbar_page.navigate()

    login_user_page.verify_on_homepage()

    return login_user_page
