import pytest

from pages.main_page import Main
from pages.sign_up_login_page import SignUpLogin
from pages.enter_account_information_page import EnterAccountInformation
from pages.account_created_page import AccountCreated
from pages.account_deleted_page import AccountDeleted
from pages.test_cases_page import TestCases
from pages.products_page import Products
from pages.product_detail_page import ProductDetail
from pages.cart_page import Cart
from pages.address_details_page import AddressDetails
from pages.payment_page import Payment
from pages.order_placed_page import OrderPlaced
from pages.contact_us_page import ContactUs
from utils.tools import take_screenshot


class Test:
    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.main = Main(self.page)
        self.sign_up_login_page = SignUpLogin(self.page)
        self.enter_account_information = EnterAccountInformation(self.page)
        self.account_created_page = AccountCreated(self.page)
        self.account_deleted_page = AccountDeleted(self.page)
        self.test_cases_page = TestCases(self.page)
        self.products_page = Products(self.page)
        self.product_detail_page = ProductDetail(self.page)
        self.cart_page = Cart(self.page)
        self.address_details_page = AddressDetails(self.page)
        self.payment_page = Payment(self.page)
        self.order_placed_page = OrderPlaced(self.page)
        self.contact_us_page = ContactUs(self.page)

    def test_register_user(self, test_setup):
        self.main.check_main_page_is_opened()
        self.main.click_on_sign_up_login_button()
        self.sign_up_login_page.check_new_user_sign_up_label_is_visible()
        self.sign_up_login_page.enter_name("Thomas")
        self.sign_up_login_page.enter_email("thomas@email.com")
        self.sign_up_login_page.click_on_sign_up_button()
        self.enter_account_information.check_enter_account_information_label_is_visible()
        self.enter_account_information.enter_valid_data()
        self.account_created_page.account_created_mesage_is_visible()
        self.account_created_page.click_on_continue_button()
        self.main.check_logged_in_username('Thomas')
        self.main.click_on_delete_account_button()
        self.account_deleted_page.account_deleted_message_is_visible()
        self.account_deleted_page.click_on_continue_button()

    def test_valid_login(self, test_setup):
        self.main.check_main_page_is_opened()
        self.main.click_on_sign_up_login_button()
        self.sign_up_login_page.check_new_user_sign_up_label_is_visible()
        self.sign_up_login_page.enter_name('Thomas')
        self.sign_up_login_page.enter_email('thomas@email.com')
        self.sign_up_login_page.click_on_sign_up_button()
        self.enter_account_information.check_enter_account_information_label_is_visible()
        self.enter_account_information.enter_valid_data()
        self.account_created_page.account_created_mesage_is_visible()
        self.account_created_page.click_on_continue_button()
        self.main.check_logged_in_username('Thomas')
        self.main.click_on_logout_button()
        self.sign_up_login_page.check_new_user_sign_up_label_is_visible()
        self.sign_up_login_page.enter_login_email('thomas@email.com')
        self.sign_up_login_page.enter_login_password('asdfg')
        self.sign_up_login_page.click_on_login_button()
        self.main.check_logged_in_username('Thomas')
        self.main.click_on_delete_account_button()
        self.account_deleted_page.account_deleted_message_is_visible()

    def test_invalid_login(self, test_setup):
        self.main.check_main_page_is_opened()
        self.main.click_on_sign_up_login_button()
        self.sign_up_login_page.check_new_user_sign_up_label_is_visible()
        self.sign_up_login_page.enter_login_email('qwerty@email.com')
        self.sign_up_login_page.enter_login_password('qwerty')
        self.sign_up_login_page.click_on_login_button()
        self.sign_up_login_page.check_error_message_is_visible()

    def test_logout(self, test_setup):
        self.main.check_main_page_is_opened()
        self.main.click_on_sign_up_login_button()
        self.sign_up_login_page.check_new_user_sign_up_label_is_visible()
        self.sign_up_login_page.enter_name('Thomas')
        self.sign_up_login_page.enter_email('thomas@email.com')
        self.sign_up_login_page.click_on_sign_up_button()
        self.enter_account_information.check_enter_account_information_label_is_visible()
        self.enter_account_information.enter_valid_data()
        self.account_created_page.account_created_mesage_is_visible()
        self.account_created_page.click_on_continue_button()
        self.main.check_logged_in_username('Thomas')
        self.main.click_on_logout_button()
        self.sign_up_login_page.check_new_user_sign_up_label_is_visible()
        self.sign_up_login_page.enter_login_email('thomas@email.com')
        self.sign_up_login_page.enter_login_password('asdfg')
        self.sign_up_login_page.click_on_login_button()
        self.main.check_logged_in_username('Thomas')
        self.main.click_on_logout_button()
        self.sign_up_login_page.check_new_user_sign_up_label_is_visible()
        self.sign_up_login_page.enter_login_email('thomas@email.com')
        self.sign_up_login_page.enter_login_password('asdfg')
        self.sign_up_login_page.click_on_login_button()
        self.main.check_logged_in_username('Thomas')
        self.main.click_on_delete_account_button()
        self.account_deleted_page.account_deleted_message_is_visible()

    def test_register_with_existing_email(self, test_setup):
        self.main.check_main_page_is_opened()
        self.main.click_on_sign_up_login_button()
        self.sign_up_login_page.check_new_user_sign_up_label_is_visible()
        self.sign_up_login_page.enter_name('Thomas')
        self.sign_up_login_page.enter_email('thomas@email.com')
        self.sign_up_login_page.click_on_sign_up_button()
        self.enter_account_information.check_enter_account_information_label_is_visible()
        self.enter_account_information.enter_valid_data()
        self.account_created_page.account_created_mesage_is_visible()
        self.account_created_page.click_on_continue_button()
        self.main.check_logged_in_username('Thomas')
        self.main.click_on_logout_button()
        self.sign_up_login_page.check_new_user_sign_up_label_is_visible()
        self.main.click_on_sign_up_login_button()
        self.sign_up_login_page.check_new_user_sign_up_label_is_visible()
        self.sign_up_login_page.enter_name('John')
        self.sign_up_login_page.enter_email('thomas@email.com')
        self.sign_up_login_page.click_on_sign_up_button()
        self.sign_up_login_page.check_email_error_message_is_visible()
        self.sign_up_login_page.enter_login_email('thomas@email.com')
        self.sign_up_login_page.enter_login_password('asdfg')
        self.sign_up_login_page.click_on_login_button()
        self.main.check_logged_in_username('Thomas')
        self.main.click_on_delete_account_button()
        self.account_deleted_page.account_deleted_message_is_visible()

    def test_contact_us_form(self, test_setup):
        self.main.check_main_page_is_opened()
        self.main.click_on_contact_us_button()
        self.contact_us_page.get_in_touch_is_visible()
        self.contact_us_page.enter_valid_get_in_touch_data()
        self.contact_us_page.upload_file()
        self.contact_us_page.click_on_submit_button()
        self.contact_us_page.success_message_is_visible()

    def test_test_cases_page(self, test_setup):
        self.main.check_main_page_is_opened()
        self.main.click_on_test_cases_button()
        self.test_cases_page.check_test_cases_label_is_visible()

    def test_all_products_and_product_detail_page(self, test_setup):
        self.main.check_main_page_is_opened()
        self.main.click_on_products_button()
        self.products_page.check_all_products_title_is_visible()
        self.products_page.check_all_products_list_is_visible()
        self.products_page.click_on_blue_top_view_product()
        self.product_detail_page.check_write_your_review_bar_is_visible()
        self.product_detail_page.check_product_name_is_visible()
        self.product_detail_page.check_category_is_visible()
        self.product_detail_page.check_price_is_visible()
        self.product_detail_page.check_availability_is_visible()
        self.product_detail_page.check_condition_is_visible()
        self.product_detail_page.check_brand_is_visible()

    def test_search_product(self, test_setup):
        searched_product = 'Winter Top'
        self.main.check_main_page_is_opened()
        self.main.click_on_products_button()
        self.products_page.check_all_products_title_is_visible()
        self.products_page.enter_product_name_in_search_field(searched_product)
        self.products_page.click_on_search_button()
        self.products_page.check_found_product_is_visible(searched_product)

    def test_subscription_in_home_page(self, test_setup):
        self.main.check_main_page_is_opened()
        self.main.check_subscription_text_is_visible()
        self.main.enter_email_in_your_email_address_field('qwerty@email.com')
        self.main.click_on_subscribe_button()
        self.main.success_message_is_visible('You have been successfully subscribed!')

    def test_subscription_in_cart_page(self, test_setup):
        self.main.check_main_page_is_opened()
        self.main.click_on_cart_button()
        self.cart_page.shopping_cart_text_is_visible()
        self.main.check_subscription_text_is_visible()
        self.main.enter_email_in_your_email_address_field('qwerty@email.com')
        self.main.click_on_subscribe_button()
        self.main.success_message_is_visible('You have been successfully subscribed!')

    def test_adding_products_in_cart(self, test_setup):
        self.main.check_main_page_is_opened()
        self.main.click_on_products_button()
        blue_top = "Blue Top"
        men_tshirt = "Men Tshirt"
        top_price = self.products_page.get_product_price(blue_top)
        tshirt_price = self.products_page.get_product_price(men_tshirt)
        self.products_page.add_product_to_cart(blue_top)
        self.products_page.check_added_message_is_visible()
        self.products_page.click_on_continue_shopping_button()
        self.products_page.add_product_to_cart(men_tshirt)
        self.products_page.check_added_message_is_visible()
        self.products_page.click_on_view_cart_link()
        self.cart_page.shopping_cart_text_is_visible()
        self.cart_page.check_product_exists(blue_top)
        self.cart_page.check_product_exists(men_tshirt)
        self.cart_page.check_product_quantity("0","1")
        self.cart_page.check_product_quantity("1","1")
        self.cart_page.check_product_price("0",top_price)
        self.cart_page.check_product_price("1",tshirt_price)

    def test_product_quantity_in_cart(self, test_setup):
        self.main.check_main_page_is_opened()
        self.main.click_on_view_product_button()
        self.product_detail_page.check_product_name_is_visible()
        quantity = '4'
        self.product_detail_page.enter_quantity(quantity)
        self.product_detail_page.click_on_add_to_cart_button()
        self.product_detail_page.success_message_is_visible()
        self.product_detail_page.click_on_view_cart_button()
        self.cart_page.check_product_quantity("0", quantity)

    def test_register_while_checkout(self, test_setup):
        self.main.check_main_page_is_opened()
        blue_top = 'Blue Top'
        self.main.add_product_to_cart(blue_top)
        self.main.click_on_view_cart_link()
        self.cart_page.shopping_cart_text_is_visible()
        self.cart_page.click_on_proceed_to_checkout_button()
        self.cart_page.checkout_message_is_visible()
        self.cart_page.click_on_register_login_link()
        self.sign_up_login_page.check_new_user_sign_up_label_is_visible()
        self.sign_up_login_page.enter_name("Thomas")
        self.sign_up_login_page.enter_email("thomas@email.com")
        self.sign_up_login_page.click_on_sign_up_button()
        self.enter_account_information.check_enter_account_information_label_is_visible()
        self.enter_account_information.enter_valid_data()
        self.account_created_page.account_created_mesage_is_visible()
        self.account_created_page.click_on_continue_button()
        self.main.check_logged_in_username('Thomas')
        self.main.click_on_cart_button()
        self.cart_page.click_on_proceed_to_checkout_button()
        self.address_details_page.check_address_details_header_is_visible()
        self.address_details_page.check_review_your_order_header_is_visible()
        self.address_details_page.enter_text_in_text_area('qwertyqwerty')
        self.address_details_page.click_on_place_order_button()
        self.payment_page.check_payment_header_is_visible()
        self.payment_page.check_payment_fields_are_visible()
        self.payment_page.enter_valid_payment_data()
        self.payment_page.click_pay_and_confirm_button()
        self.order_placed_page.check_success_message_is_visible()
        self.order_placed_page.click_on_delete_account_button()
        self.account_deleted_page.account_deleted_message_is_visible()

    def test_register_before_checkout(self, test_setup):
        self.main.check_main_page_is_opened()
        self.main.click_on_sign_up_login_button()
        self.sign_up_login_page.enter_name("Thomas")
        self.sign_up_login_page.enter_email("thomas@email.com")
        self.sign_up_login_page.click_on_sign_up_button()
        self.enter_account_information.check_enter_account_information_label_is_visible()
        self.enter_account_information.enter_valid_data()
        self.account_created_page.account_created_mesage_is_visible()
        self.account_created_page.click_on_continue_button()
        self.main.check_logged_in_username('Thomas')
        blue_top = 'Blue Top'
        self.main.add_product_to_cart(blue_top)
        self.main.click_on_view_cart_link()
        self.cart_page.shopping_cart_text_is_visible()
        self.cart_page.click_on_proceed_to_checkout_button()
        self.address_details_page.check_address_details_header_is_visible()
        self.address_details_page.check_review_your_order_header_is_visible()
        self.address_details_page.enter_text_in_text_area('qwertyqwerty')
        self.address_details_page.click_on_place_order_button()
        self.payment_page.check_payment_header_is_visible()
        self.payment_page.check_payment_fields_are_visible()
        self.payment_page.enter_valid_payment_data()
        self.payment_page.click_pay_and_confirm_button()
        self.order_placed_page.check_success_message_is_visible()
        self.order_placed_page.click_on_delete_account_button()
        self.account_deleted_page.account_deleted_message_is_visible()

















