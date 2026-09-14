from playwright.sync_api import Page, expect


class PaymentPage:
    def __init__(self, page: Page):
        self.page = page

        self.delivery_address = page.locator("#address_delivery")
        self.delivery_name = self.delivery_address.locator(
            ".address_firstname.address_lastname"
        )
        self.delivery_address_lines = self.delivery_address.locator(
            ".address_address1.address_address2"
        )
        self.delivery_location = self.delivery_address.locator(
            ".address_city.address_state_name.address_postcode"
        )
        self.delivery_country = self.delivery_address.locator(".address_country_name")
        self.delivery_phone = self.delivery_address.locator(".address_phone")
        self.download_invoice_button = page.get_by_role(
            "link",
            name="Download Invoice",
            exact=True,
        )
        self.name_on_card_input = page.locator('[data-qa="name-on-card"]')
        self.card_number_input = page.locator('[data-qa="card-number"]')
        self.cvc_input = page.locator('[data-qa="cvc"]')
        self.expiry_month_input = page.locator('[data-qa="expiry-month"]')
        self.expiry_year_input = page.locator('[data-qa="expiry-year"]')
        self.pay_button = page.locator('[data-qa="pay-button"]')

    def verify_delivery_address(
        self,
        name,
        company,
        address1,
        address2,
        city,
        state,
        zipcode,
        country,
        mobile_number,
    ):
        expect(self.delivery_name).to_contain_text(name)
        expect(self.delivery_address_lines.filter(has_text=company)).to_be_visible()
        expect(self.delivery_address_lines.filter(has_text=address1)).to_be_visible()
        expect(self.delivery_address_lines.filter(has_text=address2)).to_be_visible()
        expect(self.delivery_location).to_contain_text(city)
        expect(self.delivery_location).to_contain_text(state)
        expect(self.delivery_location).to_contain_text(zipcode)
        expect(self.delivery_country).to_have_text(country)
        expect(self.delivery_phone).to_have_text(mobile_number)

    def download_invoice(self):
        with self.page.expect_download() as download_info:
            self.download_invoice_button.click()

        return download_info.value

    def payment(
        self,
        name_on_card: str,
        card_number: str,
        cvc: str,
        expiry_month: str,
        expiry_year: str,
    ):
        self.name_on_card_input.fill(name_on_card)
        self.card_number_input.fill(card_number)
        self.cvc_input.fill(cvc)
        self.expiry_month_input.fill(expiry_month)
        self.expiry_year_input.fill(expiry_year)
        self.pay_button.click()

        expect(
            self.page.get_by_role("heading", name="Order Placed!", exact=True)
        ).to_be_visible()

        expect(
            self.page.get_by_text(
                "Congratulations! Your order has been confirmed!", exact=True
            )
        ).to_be_visible()
