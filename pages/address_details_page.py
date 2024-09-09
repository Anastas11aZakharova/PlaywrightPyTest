from playwright.sync_api import Page, expect


class AddressDetails():
    def __init__(self, page: Page):
        self.page = page

        self.__address_details_header = self.page.get_by_text('Address Details')
        self.__review_your_order_header = self.page.get_by_text('Review Your Order')
        self.__text_area = self.page.locator('textarea[class="form-control"]')
        self.__place_order_button = self.page.get_by_text('Place Order')

    def check_address_details_header_is_visible(self) -> None:
        self.__address_details_header.wait_for(state='visible')
        expect(self.__address_details_header).to_be_visible()

    def check_review_your_order_header_is_visible(self) -> None:
        self.__review_your_order_header.wait_for(state='visible')
        expect(self.__review_your_order_header).to_be_visible()

    def enter_text_in_text_area(self, text) -> None:
        self.__text_area.fill(text)

    def click_on_place_order_button(self) -> None:
        self.__place_order_button.click()
