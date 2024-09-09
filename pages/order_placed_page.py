from playwright.sync_api import Page, expect


class OrderPlaced():
    def __init__(self, page: Page):
        self.page = page

        self.__success_message = self.page.get_by_text('Congratulations! Your order has been confirmed!')
        self.__delete_account_btn = self.page.locator('a[href="/delete_account"]')

    def check_success_message_is_visible(self) -> None:
        self.__success_message.wait_for(state='visible')
        expect(self.__success_message).to_be_visible()

    def click_on_delete_account_button(self) -> None:
        self.__delete_account_btn.click()
