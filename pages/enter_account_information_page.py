from playwright.sync_api import Page, expect


class EnterAccountInformation():
    def __init__(self, page: Page):
        self.page = page

        self.__enter_account_information_label = self.page.get_by_text('Enter Account Information')
        self.__title_radio_button = self.page.locator('input[id="id_gender1"]')
        self.__name_field = self.page.locator('input[data-qa="name"]')
        self.__email_field = self.page.locator('input[data-qa="email"]')
        self.__password_field = self.page.locator('input[data-qa="password"]')
        self.__date_of_birth_day_drop_down = self.page.locator('select[data-qa="days"]')
        self.__date_of_birth_month_drop_down = self.page.locator('select[data-qa="months"]')
        self.__date_of_birth_year_drop_down = self.page.locator('select[data-qa="years"]')
        self.__newsletter_checkbox = self.page.locator('input[id="newsletter"]')
        self.__special_offers_checkbox = self.page.locator('input[id="optin"]')
        self.__address_information_first_name = self.page.locator('input[data-qa="first_name"]')
        self.__address_information_last_name = self.page.locator('input[data-qa="last_name"]')
        self.__address_information_company = self.page.locator('input[data-qa="company"]')
        self.__address_information_address = self.page.locator('input[data-qa="address"]')
        self.__address_information_address2 = self.page.locator('input[data-qa="address2"]')
        self.__address_information_country_dropdown = self.page.locator('select[data-qa="country"]')
        self.__address_information_state = self.page.locator('input[data-qa="state"]')
        self.__address_information_city = self.page.locator('input[data-qa="city"]')
        self.__address_information_zip_code = self.page.locator('input[data-qa="zipcode"]')
        self.__address_information_mobile_number = self.page.locator('input[data-qa="mobile_number"]')
        self.__address_information_create_account_btn = self.page.locator('button[data-qa="create-account"]')

    def check_enter_account_information_label_is_visible(self) -> None:
        self.__enter_account_information_label.wait_for(state='visible')
        expect(self.__enter_account_information_label).to_be_visible()

    def enter_valid_data(self, password, birth_day, birth_month, birth_year, first_name, last_name, company_name,
                         address_1, address_2, country, state, city, zip_code, mobile) -> None:
        self.__title_radio_button.check()
        self.__password_field.fill(password)
        self.__date_of_birth_day_drop_down.select_option(str(birth_day))
        self.__date_of_birth_month_drop_down.select_option(birth_month)
        self.__date_of_birth_year_drop_down.select_option(str(birth_year))
        self.__newsletter_checkbox.check()
        self.__special_offers_checkbox.check()
        self.__address_information_first_name.fill(first_name)
        self.__address_information_last_name.fill(last_name)
        self.__address_information_company.fill(company_name)
        self.__address_information_address.fill(address_1)
        self.__address_information_address2.fill(address_2)
        self.__address_information_country_dropdown.select_option(country)
        self.__address_information_state.fill(state)
        self.__address_information_city.fill(city)
        self.__address_information_zip_code.fill(zip_code)
        self.__address_information_mobile_number.fill(str(mobile))
        self.__address_information_create_account_btn.click()
