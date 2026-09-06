import pytest
from playwright.sync_api import Page
from pages.login_user_page import LoginPage
from pages.register_user_page import RegistrationPage


# =========================================================================
# TEST CASE 2: CORRECT LOGIN
# =========================================================================
def test_login_correct_user(page: Page):
    register_user_page = RegistrationPage(page)

    login_user_page = LoginPage(page)

    login_user_page.navigate()
    login_user_page.go_to_login()
    login_user_page.verify_login_page()

    login_user_page.login("junueljonn@gmail.com", "password123")

    login_user_page.verify_logged_in_user()

    # register_user_page.delete_account()

    # register_user_page.verify_account_deleted()


# =========================================================================
# TEST CASE 3: INCORRECT LOGIN
# =========================================================================


def test_login_incorrect_user(page: Page, launch_browser):
    register_user_page = RegistrationPage(page)
    login_user_page = launch_browser

    login_user_page.go_to_login()

    login_user_page.verify_login_page()

    login_user_page = LoginPage(page)

    login_user_page.login("junuelincorrect@gmail.com", "password123")

    login_user_page.verify_logged_in_user_incorrect()


# =========================================================================
# TEST CASE 4: LOGOUT USER
# =========================================================================


def test_logout_user(page: Page, launch_browser):
    register_user_page = RegistrationPage(page)
    login_user_page = launch_browser

    login_user_page.go_to_login()

    login_user_page.verify_login_page()

    login_user_page = LoginPage(page)

    login_user_page.verify_login_page()

    login_user_page.login("junueljonn@gmail.com", "password123")

    login_user_page.verify_logged_in_user()

    login_user_page.logout_user()

    login_user_page.verify_login_page()
