import pytest
from playwright.sync_api import Page
from pages.login_user_page import LoginPage
from pages.contact_page import ContactPage
from pages.navbar_page import NavbarPage


def test_contact_us_form(page: Page, setup_browser):

    login_user_page = setup_browser

    contact_page = ContactPage(page)

    # navbar_page = NavbarPage(page)
    # navbar_page.go_to_contact()
    contact_page.go_to_contact()

    contact_page.verify_get_in_touch()

    contact_page.contact_us_form_fill(
        "junuel", "junuel@example.com", "Test Subject", "Test Message"
    )

    # contact_page.upload_file("/home/a_c/Downloads/test.txt")

    contact_page.submit_form()

    contact_page.verify_successful_submission()

    contact_page.go_to_home()

    login_user_page.verify_on_homepage()
