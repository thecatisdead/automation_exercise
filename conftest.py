import pytest

from playwright.sync_api import Page, sync_playwright

from pages.login_user_page import LoginPage
from pages.navbar_page import NavbarPage


@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            # executable_path="/usr/bin/brave-browser",
            headless=False,
            slow_mo=800,
        )

        page = browser.new_page()
        yield page

        # input("Press Enter to close...")
        browser.close()


@pytest.fixture
def launch_browser(page: Page):
    login_user_page = LoginPage(page)

    navbar_page = NavbarPage(page)
    navbar_page.navigate()

    login_user_page.verify_on_homepage()

    return login_user_page


# import pytest
# from playwright.sync_api import sync_playwright

# from pages.login_user_page import LoginPage
# from pages.navbar_page import NavbarPage


# @pytest.fixture(scope="session")
# def playwright_instance():
#     with sync_playwright() as p:
#         yield p


# @pytest.fixture(scope="session")
# def browser(playwright_instance):
#     browser = playwright_instance.chromium.launch(
#         # executable_path="/usr/bin/brave-browser",  # drop this to use bundled Chromium (faster)
#         headless=True,  # flip to False only when actively debugging
#     )
#     yield browser
#     browser.close()


# @pytest.fixture
# def page(browser):
#     context = browser.new_context()
#     page = context.new_page()
#     yield page
#     context.close()


# @pytest.fixture
# def launch_browser(page):
#     login_user_page = LoginPage(page)

#     navbar_page = NavbarPage(page)
#     navbar_page.navigate()

#     login_user_page.verify_on_homepage()

#     return login_user_page
