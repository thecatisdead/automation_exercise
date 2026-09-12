import pytest
from playwright.sync_api import Page
from pages.navbar_page import NavbarPage
from pages.register_user_page import RegistrationPage

# =========================================================================
# TEST CASE 1: REGISTER USER
# =========================================================================


def test_register_user(page: Page, setup_browser, user_info, delete_account):
    setup_browser

    register_user_page = RegistrationPage(page)
    navbar_page = NavbarPage(page)

    navbar_page.go_to_login_signup()

    register_user_page.verify_new_user_signup()

    register_user_page.signup("junuel", "junuelregisterusertest105@gmail.com")

    user_info()

    delete_account()
