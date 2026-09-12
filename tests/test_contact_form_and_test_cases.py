import pytest
from playwright.sync_api import Page
from pages.login_user_page import LoginPage
from pages.contact_page import ContactPage
from pages.navbar_page import NavbarPage
from pages.hompage_page import HomePage

# =========================================================================
# TEST CASE 6: CONTACT US FORM
# =========================================================================


def test_contact_us_form(page: Page, setup_browser):

    setup_browser
    homepage_page = HomePage(page)
    contact_page = ContactPage(page)
    navbar_page = NavbarPage(page)

    navbar_page.go_to_contact()

    navbar_page.verify_contact_us_form()

    contact_page.verify_get_in_touch()

    contact_page.contact_us_form_fill(
        "junuel", "junuel@example.com", "Test Subject", "Test Message"
    )

    contact_page.upload_file("/home/a_c/Downloads/test.txt")

    contact_page.submit_form()

    contact_page.verify_successful_submission()

    contact_page.go_to_home()

    homepage_page.verify_on_homepage()


# =========================================================================
# TEST CASE 7: VERIFY TEST CASES PAGE
# =========================================================================


def test_navigation_test_case(page: Page, setup_browser):
    setup_browser

    navbar_page = NavbarPage(page)

    navbar_page.go_to_test_cases()

    navbar_page.verify_on_test_cases_page()
