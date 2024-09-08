import pytest
from playwright.sync_api import expect

from pages.main_page import Main
from pages.sign_up_login_page import SignUpLogin
from pages.enter_account_information_page import EnterAccountInformation
from pages.account_created_page import AccountCreated
from pages.account_deleted_page import AccountDeleted
from pages.test_cases_page import TestCases
from pages.products_page import Products
from pages.product_detail_page import ProductDetail
from pages.cart_page import Cart
from utils.tools import take_screenshot


class Test:
    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.main = Main(self.page)
        self.sign_up_login = SignUpLogin(self.page)
        self.enter_account_information = EnterAccountInformation(self.page)
        self.account_created_page = AccountCreated(self.page)
        self.account_deleted_page = AccountDeleted(self.page)
        self.test_cases_page = TestCases(self.page)
        self.products_page = Products(self.page)
        self.product_detail_page = ProductDetail(self.page)
        self.cart_page = Cart(self.page)

    # def test_register_user(self, test_setup):
    #     self.main.check_main_page_is_opened()
    #     self.main.click_on_sign_up_login_button()
    #     self.sign_up_login.check_new_user_sign_up_label_is_visible()
    #     self.sign_up_login.enter_name("Thomas")
    #     self.sign_up_login.enter_email("thomas@email.com")
    #     self.sign_up_login.click_on_sign_up_button()
    #     self.enter_account_information.check_enter_account_information_label_is_visible()
    #     self.enter_account_information.enter_valid_data()
    #     self.account_created_page.account_created_mesage_is_visible()
    #     self.account_created_page.click_on_continue_button()
    #     self.main.check_logged_in_username('Thomas')
    #     self.main.click_on_delete_account_button()
    #     self.account_deleted_page.account_deleted_message_is_visible()
    #     self.account_deleted_page.click_on_continue_button()

    # def test_valid_login(self, test_setup):
    #     self.main.check_main_page_is_opened()
    #     self.main.click_on_sign_up_login_button()
    #     self.sign_up_login.check_new_user_sign_up_label_is_visible()
    #     self.sign_up_login.enter_name('Thomas')
    #     self.sign_up_login.enter_email('thomas@email.com')
    #     self.sign_up_login.click_on_sign_up_button()
    #     self.enter_account_information.check_enter_account_information_label_is_visible()
    #     self.enter_account_information.enter_valid_data()
    #     self.account_created_page.account_created_mesage_is_visible()
    #     self.account_created_page.click_on_continue_button()
    #     self.main.check_logged_in_username('Thomas')
    #     self.main.click_on_logout_button()
    #     self.sign_up_login.check_new_user_sign_up_label_is_visible()
    #     self.sign_up_login.enter_login_email('thomas@email.com')
    #     self.sign_up_login.enter_login_password('asdfg')
    #     self.sign_up_login.click_on_login_button()
    #     self.main.check_logged_in_username('Thomas')
    #     self.main.click_on_delete_account_button()
    #     self.account_deleted_page.account_deleted_message_is_visible()
    #
    #
    # def test_invalid_login(self, test_setup):
    #     self.main.check_main_page_is_opened()
    #     self.main.click_on_sign_up_login_button()
    #     self.sign_up_login.check_new_user_sign_up_label_is_visible()
    #     self.sign_up_login.enter_login_email('qwerty@email.com')
    #     self.sign_up_login.enter_login_password('qwerty')
    #     self.sign_up_login.click_on_login_button()
    #     self.sign_up_login.check_error_message_is_visible()

    # def test_logout(self, test_setup):
    #     self.main.check_main_page_is_opened()
    #     self.main.click_on_sign_up_login_button()
    #     self.sign_up_login.check_new_user_sign_up_label_is_visible()
    #     self.sign_up_login.enter_name('Thomas')
    #     self.sign_up_login.enter_email('thomas@email.com')
    #     self.sign_up_login.click_on_sign_up_button()
    #     self.enter_account_information.check_enter_account_information_label_is_visible()
    #     self.enter_account_information.enter_valid_data()
    #     self.account_created_page.account_created_mesage_is_visible()
    #     self.account_created_page.click_on_continue_button()
    #     self.main.check_logged_in_username('Thomas')
    #     self.main.click_on_logout_button()
    #     self.sign_up_login.check_new_user_sign_up_label_is_visible()
    #     self.sign_up_login.enter_login_email('thomas@email.com')
    #     self.sign_up_login.enter_login_password('asdfg')
    #     self.sign_up_login.click_on_login_button()
    #     self.main.check_logged_in_username('Thomas')
    #     self.main.click_on_logout_button()
    #     self.sign_up_login.check_new_user_sign_up_label_is_visible()
    #     self.main.click_on_delete_account_button()

    # def test_register_with_existing_email(self, test_setup):
    #     self.main.check_main_page_is_opened()
    #     self.main.click_on_sign_up_login_button()
    #     self.sign_up_login.check_new_user_sign_up_label_is_visible()
    #     self.sign_up_login.enter_name('Thomas')
    #     self.sign_up_login.enter_email('thomas@email.com')
    #     self.sign_up_login.click_on_sign_up_button()
    #     self.enter_account_information.check_enter_account_information_label_is_visible()
    #     self.enter_account_information.enter_valid_data()
    #     self.account_created_page.account_created_mesage_is_visible()
    #     self.account_created_page.click_on_continue_button()
    #     self.main.check_logged_in_username('Thomas')
    #     self.main.click_on_logout_button()
    #     self.sign_up_login.check_new_user_sign_up_label_is_visible()
    #     self.main.click_on_sign_up_login_button()
    #     self.sign_up_login.check_new_user_sign_up_label_is_visible()
    #     self.sign_up_login.enter_name('John')
    #     self.sign_up_login.enter_email('thomas@email.com')
    #     self.sign_up_login.click_on_sign_up_button()
    #     self.sign_up_login.check_email_error_message_is_visible()
    #     self.main.click_on_delete_account_button()

    def test_test_cases_page(self, test_setup):
        self.main.check_main_page_is_opened()
        self.main.click_on_test_cases_button()
        self.test_cases_page.check_test_cases_label_is_visible()

    # def test_all_products_and_product_detail_page(self, test_setup):
    #     self.main.check_main_page_is_opened()
    #     self.main.click_on_products_button()
    #     self.products_page.check_all_products_title_is_visible()
    #     self.products_page.check_all_products_list_is_visible()
    #     self.products_page.click_on_blue_top_view_product()
    #     self.product_detail_page.check_write_your_review_bar_is_visible()
    #     self.product_detail_page.check_product_name_is_visible()
    #     self.product_detail_page.check_category_is_visible()
    #     self.product_detail_page.check_price_is_visible()
    #     self.product_detail_page.check_availability_is_visible()
    #     self.product_detail_page.check_condition_is_visible()
    #     self.product_detail_page.check_brand_is_visible()
        # self.page.pause()

    # def test_search_product(self, test_setup):
    #     searched_product = 'Winter Top'
    #     self.main.check_main_page_is_opened()
    #     self.main.click_on_products_button()
    #     self.products_page.check_all_products_title_is_visible()
    #     self.products_page.enter_product_name_in_search_field(searched_product)
    #     self.products_page.click_on_search_button()
    #     self.products_page.check_found_product_is_visible(searched_product)
    #     self.page.pause()

    # def test_subscription_in_home_page(self, test_setup):
    #     self.main.check_main_page_is_opened()
    #     self.main.check_subscription_text_is_visible()
    #     self.main.enter_email_in_your_email_address_field('qwerty@email.com')
    #     self.main.click_on_subscribe_button()
    #     self.main.success_message_is_visible('You have been successfully subscribed!')
    #     self.page.pause()

    # def test_subscription_in_cart_page(self, test_setup):
    #     self.main.check_main_page_is_opened()
    #     self.main.click_on_cart_button()
    #     self.cart_page.shopping_cart_text_is_visible()
    #     self.main.check_subscription_text_is_visible()
    #     self.main.enter_email_in_your_email_address_field('qwerty@email.com')
    #     self.main.click_on_subscribe_button()
    #     self.main.success_message_is_visible('You have been successfully subscribed!')
    #     self.page.pause()

    # def test_adding_products_in_cart(self, test_setup):
    #     self.main.check_main_page_is_opened()
    #     self.main.click_on_products_button()
    #     blue_top = "Blue Top"
    #     men_tshirt = "Men Tshirt"
    #     top_price = self.products_page.get_product_price(blue_top)
    #     tshirt_price = self.products_page.get_product_price(men_tshirt)
    #     self.products_page.add_product_to_cart(blue_top)
    #     self.products_page.check_added_message_is_visible()
    #     self.products_page.click_on_continue_shopping_button()
    #     self.products_page.add_product_to_cart(men_tshirt)
    #     self.products_page.check_added_message_is_visible()
    #     self.products_page.click_on_view_cart_link()
    #     self.cart_page.shopping_cart_text_is_visible()
    #     self.cart_page.check_product_exists(blue_top)
    #     self.cart_page.check_product_exists(men_tshirt)
    #     self.cart_page.check_product_quantity("0","1")
    #     self.cart_page.check_product_quantity("1","1")
    #     self.cart_page.check_product_price("0",top_price)
    #     self.cart_page.check_product_price("1",tshirt_price)



        self.page.pause()


        # self.main.click_on_cart_button()
        # self.cart_page.shopping_cart_text_is_visible()
        # self.main.check_subscription_text_is_visible()
        # self.main.enter_email_in_your_email_address_field('qwerty@email.com')
        # self.main.click_on_subscribe_button()
        # self.main.success_message_is_visible('You have been successfully subscribed!')

















