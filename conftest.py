import pytest

from playwright.sync_api import Page, sync_playwright

from pages.login_user_page import LoginPage


@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path="/usr/bin/brave-browser",
            headless=False,
            slow_mo=1000,
        )

        page = browser.new_page()
        yield page

        # input("Press Enter to close...")
        browser.close()


@pytest.fixture
def logged_in(page: Page):
    login_user_page = LoginPage(page)

    login_user_page.navigate()

    login_user_page.verify_on_homepage()

    return login_user_page
