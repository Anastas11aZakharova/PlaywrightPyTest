from playwright.sync_api import Page, expect


class Main():
    def __init__(self, page: Page):
        self.page = page

        self.__main_logo = self.page.locator('img[src="/static/images/home/logo.png"]')
        self.__consent_button = self.page.locator('button[aria-label="Consent"]')
        self.__sign_up_login_button = self.page.locator('a[href="/login"]')
        self.__logged_in_as_label = self.page.locator('xpath=//a[contains(text(),\'Logged in as\')]')
        self.__delete_account_button = self.page.locator('a[href="/delete_account"]')
        self.__logout_button = self.page.locator('a[href="/logout"]')
        self.__test_cases_button = self.page.locator('a[href="/test_cases"]').locator("nth=0")
        self.__products_button = self.page.locator('a[href="/products"]')
        self.__subscription_text = self.page.get_by_text('Subscription')
        self.__your_email_address_field = self.page.locator('input[id="susbscribe_email"]')
        self.__subscribe_button = self.page.locator('button[id="subscribe"]')
        self.__success_message = self.page.locator('div[id="success-subscribe"]')
        self.__cart_button = self.page.locator('a[href="/view_cart"]').locator("nth=0")
        self.__view_product_button = self.page.get_by_text('View Product').locator("nth=0")
        self.__add_to_cart_button = self.page.locator('a[class="btn btn-default add-to-cart"]').locator("nth=0")
        self.__view_cart_link = self.page.locator('//a[@href=\'/view_cart\']').locator("nth=1")
        self.__contact_us_button = self.page.locator('a[href="/contact_us"]')

    def check_main_page_is_opened(self) -> None:
        self.__main_logo.wait_for(state='visible')
        expect(self.__main_logo).to_be_visible()
        if self.__consent_button.count() > 0:
            self.__consent_button.click()

    def click_on_sign_up_login_button(self) -> None:
        self.__sign_up_login_button.click()

    def check_logged_in_username(self, name) -> None:
        expect(self.__logged_in_as_label).to_have_text('Logged in as ' + name)

    def click_on_delete_account_button(self) -> None:
        self.__delete_account_button.click()

    def click_on_logout_button(self) -> None:
        self.__logout_button.click()

    def click_on_test_cases_button(self) -> None:
        self.__test_cases_button.click()

    def click_on_products_button(self) -> None:
        self.__products_button.click()

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

    def click_on_cart_button(self) -> None:
        self.__cart_button.click()

    def click_on_view_product_button(self) -> None:
        self.__view_product_button.click()

    def add_product_to_cart(self, product_name) -> None:
        self.__add_to_cart_button.click()

    def click_on_view_cart_link(self) -> None:
        self.__view_cart_link.click()

    def click_on_contact_us_button(self) -> None:
        self.__contact_us_button.click()
