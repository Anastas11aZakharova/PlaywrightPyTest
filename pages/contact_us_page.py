from playwright.sync_api import Page, expect


class ContactUs():
    def __init__(self, page: Page):
        self.page = page

        self.__get_in_touch_title = self.page.locator('h2[class="title text-center"]').locator('nth=0')
        self.__name_field = self.page.locator('input[data-qa="name"]')
        self.__email_field = self.page.locator('input[data-qa="email"]')
        self.__subject_field = self.page.locator('input[data-qa="subject"]')
        self.__your_message_here_field = self.page.locator('textarea[data-qa="message"]')
        self.__choose_file_button = self.page.locator('input[name="upload_file"]')
        self.__submit_button = self.page.locator('input[data-qa="submit-button"]')
        self.__success_message = self.page.locator('div[class="status alert alert-success"]')





    def get_in_touch_is_visible(self) -> None:
        self.__get_in_touch_title.wait_for(state='visible')
        expect(self.__get_in_touch_title).to_be_visible()

    def check_get_in_touch_fields_are_visible(self) -> None:
        self.__name_field.wait_for(state='visible')
        expect(self.__name_field).to_be_visible()
        self.__email_field.wait_for(state='visible')
        expect(self.__email_field).to_be_visible()
        self.__subject_field.wait_for(state='visible')
        expect(self.__subject_field).to_be_visible()
        self.__your_message_here_field.wait_for(state='visible')
        expect(self.__your_message_here_field).to_be_visible()

    def enter_valid_get_in_touch_data(self) -> None:
        self.__name_field.fill("Thomas")
        self.__email_field.fill("qwerty@email.com")
        self.__subject_field.fill("QWERTY")
        self.__your_message_here_field.fill("qwertyqwerty")

    def handle_dialog(self, dialog):
        if "Press OK to proceed!" in dialog.message:
            print(f'clicking "Yes" to {dialog.message}')
            dialog.accept()  # press "Yes"
        else:
            dialog.dismiss()  # press "No"

    def upload_file(self) -> None:
        self.__choose_file_button.set_input_files("data/test.txt")

    def click_on_submit_button(self) -> None:
        self.page.on("dialog", self.handle_dialog)
        self.__submit_button.click()

    def success_message_is_visible(self) -> None:
        self.__success_message.wait_for(state='visible')
        expect(self.__success_message).to_be_visible()

