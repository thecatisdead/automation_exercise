import pytest
from playwright.sync_api import Page
from pages.navbar_page import NavbarPage


def test_test_case(page: Page, setup_browser):
    setup_browser

    navbar_page = NavbarPage(page)

    navbar_page.go_to_test_cases()

    navbar_page.verify_on_test_cases_page()
