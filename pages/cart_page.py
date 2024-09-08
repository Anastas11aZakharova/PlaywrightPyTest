from playwright.sync_api import Page, expect


class Cart():
    def __init__(self, page: Page):
        self.page = page

        self.__shopping_cart_text = self.page.get_by_text('Shopping Cart')
        self.__subscription_text = self.page.get_by_text('Subscription')
        self.__your_email_address_field = self.page.locator('input[id="susbscribe_email"]')
        self.__subscribe_button = self.page.locator('button[id="subscribe"]')
        self.__success_message = self.page.locator('div[id="success-subscribe"]')
        self.__cart_info_table = self.page.locator('table[id="cart_info_table"]')


    def check_subscription_text_is_visible(self) -> None:
        self.__subscription_text.wait_for(state='visible')
        expect(self.__subscription_text).to_be_visible()

    def enter_email_in_your_email_address_field(self, email) -> None:
        self.__your_email_address_field.fill(email)

    def click_on_subscribe_button(self) -> None:
        self.__subscribe_button.click()

    def success_message_is_visible(self, text) -> None:
        self.__success_message.wait_for(state='visible')
        expect(self.__success_message).to_have_text(text)

    def shopping_cart_text_is_visible(self) -> None:
        self.__shopping_cart_text.wait_for(state='visible')
        expect(self.__shopping_cart_text).to_be_visible()

    def check_product_exists(self,product_name) -> None:
        expect(self.__cart_info_table.get_by_text(product_name)).to_be_visible()

    def check_product_quantity(self,nth,expected_quantity) -> None:
        quantity = self.__cart_info_table.locator("xpath=//td[@class='cart_quantity']/button").locator("nth=" + nth)
        expect(quantity).to_have_text(expected_quantity)

    def check_product_price(self,nth,expected_price) -> None:
        quantity = self.__cart_info_table.locator("xpath=//td[@class='cart_price']/p").locator("nth=" + nth)
        expect(quantity).to_have_text(expected_price)
