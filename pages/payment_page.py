from playwright.sync_api import Page, expect


class Payment():
    def __init__(self, page: Page):
        self.page = page

        self.__payment_header = self.page.get_by_text('Payment').locator("nth=0")
        self.__name_on_card_field = self.page.locator('input[data-qa="name-on-card"]')
        self.__card_number_field = self.page.locator('input[data-qa="card-number"]')
        self.__cvc_field = self.page.locator('input[data-qa="cvc"]')
        self.__expiration_month_field = self.page.locator('input[data-qa="expiry-month"]')
        self.__expiration_year_field = self.page.locator('input[data-qa="expiry-year"]')
        self.__pay_and_confirm_order_button = self.page.locator('button[data-qa="pay-button"]')

    def check_payment_header_is_visible(self) -> None:
        self.__payment_header.wait_for(state='visible')
        expect(self.__payment_header).to_be_visible()

    def check_payment_fields_are_visible(self) -> None:
        self.__name_on_card_field.wait_for(state='visible')
        expect(self.__card_number_field).to_be_visible()
        self.__card_number_field.wait_for(state='visible')
        expect(self.__name_on_card_field).to_be_visible()
        self.__cvc_field.wait_for(state='visible')
        expect(self.__cvc_field).to_be_visible()
        self.__expiration_month_field.wait_for(state='visible')
        expect(self.__expiration_month_field).to_be_visible()
        self.__expiration_year_field.wait_for(state='visible')
        expect(self.__expiration_year_field).to_be_visible()

    def enter_valid_payment_data(self) -> None:
        self.__name_on_card_field.fill("Thomas")
        self.__card_number_field.fill("12345678910")
        self.__cvc_field.fill("1234")
        self.__expiration_month_field.fill("January")
        self.__expiration_year_field.fill("2030")

    def click_pay_and_confirm_button(self) -> None:
        self.__pay_and_confirm_order_button.click()
