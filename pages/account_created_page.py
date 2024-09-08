from playwright.sync_api import Page, expect


class AccountCreated():
    def __init__(self, page: Page):
        self.page = page

        self.__account_created_message = self.page.get_by_text('Account Created!')
        self.__continue_btn = self.page.locator('a[data-qa="continue-button"]')


    def account_created_mesage_is_visible (self) -> None:
        self.__account_created_message.wait_for(state='visible')
        expect(self.__account_created_message).to_be_visible()
    def click_on_continue_button(self) -> None:
        self.__continue_btn.click()