import pytest
from playwright.sync_api import Page
from pages.login_user_page import LoginPage
from pages.register_user_page import RegistrationPage
from pages.navbar_page import NavbarPage


def test_register_existing_email(page: Page, setup_browser):
    register_user_page = RegistrationPage(page)
    login_user_page = setup_browser
    navbar_page = NavbarPage(page)

    login_user_page = LoginPage(page)

    navbar_page.go_to_login()

    register_user_page.verify_new_user_signup()

    register_user_page.signup("junuel", "junueljon2@gmail.com")
    register_user_page.verify_signup_error()
