from playwright.sync_api import Page, expect


class SignUpLogin():
    def __init__(self, page: Page):
        self.page = page

        self.__new_user_sign_up_label = self.page.get_by_text('New User Signup!')
        self.__name_field = self.page.locator('input[data-qa="signup-name"]')
        self.__email_field = self.page.locator('input[data-qa="signup-email"]')
        self.__sign_up_btn = self.page.locator('button[data-qa="signup-button"]')
        self.__login_email_field = self.page.locator('input[data-qa="login-email"]')
        self.__login_password_field = self.page.locator('input[data-qa="login-password"]')
        self.__login_btn = self.page.locator('button[data-qa="login-button"]')
        self.__error_message = self.page.get_by_text('Your email or password is incorrect!')
        self.__email_error_message = self.page.get_by_text('Email Address already exist!')

    def check_new_user_sign_up_label_is_visible(self) -> None:
        self.__new_user_sign_up_label.wait_for(state='visible')
        expect(self.__new_user_sign_up_label).to_be_visible()

    def enter_name(self, name) -> None:
        self.__name_field.fill(name)

    def enter_email(self, email) -> None:
        self.__email_field.fill(email)

    def click_on_sign_up_button(self) -> None:
        self.__sign_up_btn.click()

    def enter_login_email(self, email) -> None:
        self.__login_email_field.fill(email)

    def enter_login_password(self, password) -> None:
        self.__login_password_field.fill(password)

    def click_on_login_button(self) -> None:
        self.__login_btn.click()

    def check_error_message_is_visible(self) -> None:
        self.__error_message.wait_for(state='visible')
        expect(self.__error_message).to_be_visible()

    def check_email_error_message_is_visible(self) -> None:
        self.__email_error_message.wait_for(state='visible')
        expect(self.__email_error_message).to_be_visible()

        # self.page.pause()
