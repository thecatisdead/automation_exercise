from playwright.sync_api import Page, expect


class ContactPage:
    def __init__(self, page: Page):
        self.page = page
        self.page.on(
            "dialog", self._handle_dialog
        )  # persistent, registered once up front

        self.contact_us_link = page.get_by_role("link", name="Contact us")
        self.contact_heading = page.locator("h2", has_text="get in touch")
        self.name_input = page.locator("[data-qa='name']")
        self.email_input = page.locator("[data-qa='email']")
        self.subject_input = page.locator("[data-qa='subject']")
        self.message_input = page.locator("[data-qa='message']")
        self.upload_file_input = page.locator("input[name='upload_file']")
        self.submit_form_button = page.locator("[data-qa='submit-button']")
        self.home_button = page.locator("#form-section a.btn.btn-success")

    def _handle_dialog(self, dialog):
        dialog.accept()
        self.page.wait_for_timeout(
            300
        )  # gives the site's JS time to proceed after accept

    def go_to_contact(self):
        self.contact_us_link.click()

    def verify_contact_us_form(self):
        expect(self.page).to_have_url("https://automationexercise.com/contact_us")
        expect(self.contact_us_link).to_be_visible()
        expect(self.contact_us_link).to_have_text("Contact us")

    def verify_successful_submission(self):
        success = self.page.locator(".status.alert.alert-success")
        expect(success).to_be_visible(timeout=10000)
        expect(success).to_have_text(
            "Success! Your details have been submitted successfully."
        )

    def verify_get_in_touch(self):
        expect(self.contact_heading).to_be_visible()

    def contact_us_form_fill(self, name: str, email: str, subject: str, message: str):
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.subject_input.fill(subject)
        self.message_input.fill(message)

    def upload_file(self, file_path: str):
        self.upload_file_input.set_input_files(file_path)

    def submit_form(self):
        self.page.wait_for_load_state(
            "networkidle"
        )  # let the page's own JS fully finish loading/binding
        self.submit_form_button.click()

    def go_to_home(self):
        self.home_button.click()
