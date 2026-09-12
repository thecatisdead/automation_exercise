import pytest
from playwright.sync_api import Page
from pages.login_user_page import LoginPage
from pages.register_user_page import RegistrationPage
from pages.navbar_page import NavbarPage


# =========================================================================
# TEST CASE 2: CORRECT LOGIN
# =========================================================================
def test_login_correct_user(page: Page, setup_browser):

    setup_browser
    login_user_page = LoginPage(page)
    navbar_page = NavbarPage(page)

    navbar_page.go_to_login_signup()

    login_user_page.verify_login_page()

    login_user_page.login("junueljonn@gmail.com", "password123")

    login_user_page.verify_logged_in_user()


# register_user_page.delete_account()

# register_user_page.verify_account_deleted()


# =========================================================================
# TEST CASE 3: INCORRECT LOGIN
# =========================================================================


def test_login_incorrect_user(page: Page, setup_browser):
    setup_browser
    RegistrationPage(page)
    login_user_page = LoginPage(page)
    navbar_page = NavbarPage(page)

    navbar_page.go_to_login_signup()

    login_user_page.verify_login_page()

    login_user_page.login("junuelincorrect@gmail.com", "password123")

    login_user_page.verify_logged_in_user_incorrect()


# =========================================================================
# TEST CASE 4: LOGOUT USER
# =========================================================================


def test_logout_user(page: Page, setup_browser):
    setup_browser
    RegistrationPage(page)
    login_user_page = LoginPage(page)
    navbar_page = NavbarPage(page)

    navbar_page.go_to_login_signup()

    login_user_page.verify_login_page()

    login_user_page.login("junueljonn@gmail.com", "password123")

    login_user_page.verify_logged_in_user()

    navbar_page.logout_user()

    login_user_page.verify_login_page()
