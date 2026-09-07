import pytest
from playwright.sync_api import Page
from pages.navbar_page import NavbarPage
from pages.register_user_page import RegistrationPage


def test_register_user(page: Page, setup_browser):
    register_user_page = RegistrationPage(page)
    navbar_page = NavbarPage(page)

    login_user_page = setup_browser

    navbar_page.go_to_signup()

    # register_user_page.verify_on_homepage()

    # register_user_page.go_to_login()

    register_user_page.verify_new_user_signup()
    register_user_page.signup("junuel", "junueljon7@gmail.com")

    register_user_page.verify_enter_account_info()

    register_user_page.male_radio.check()

    register_user_page.enter_password("password123")

    register_user_page.select_day("2", "10", "2000")

    register_user_page.select_newsletter()
    register_user_page.select_special_offers()

    register_user_page.enter_address_info(
        first_name="junuel",
        last_name="dizon",
        company="ABC Company",
        address1="123 Main St",
        address2="Apt 4B",
        country="United States",
        city="New York",
        state="NY",
        zipcode="10001",
        mobile_number="0912345678",
    )
    register_user_page.verify_account_created()

    register_user_page.click_continue_button()

    # register_user_page.delete_account()

    # register_user_page.verify_account_deleted()

    # register_user_page.click_continue_button()
