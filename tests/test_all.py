import pytest
from faker import Faker

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
from utils.common_steps import register_new_random_user, checkout_products, perform_login, register_new_user


class Test:
    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.main_page = Main(self.page)
        self.sign_up_login_page = SignUpLogin(self.page)
        self.enter_account_information_page = EnterAccountInformation(self.page)
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

    @pytest.mark.registration_and_login
    def test_register_user(self, test_setup):
        self.main_page.check_main_page_is_opened()
        self.main_page.click_on_sign_up_login_button()
        register_new_random_user(self)
        take_screenshot(self.page, 'registered_user')
        self.main_page.click_on_delete_account_button()
        self.account_deleted_page.account_deleted_message_is_visible()
        self.account_deleted_page.click_on_continue_button()

    @pytest.mark.registration_and_login
    def test_valid_login(self, test_setup):
        fake = Faker()
        self.main_page.check_main_page_is_opened()
        self.main_page.click_on_sign_up_login_button()
        email = fake.email()
        password = fake.password()
        name = fake.first_name()
        register_new_user(self, email, password, name)
        self.main_page.click_on_logout_button()
        self.sign_up_login_page.check_new_user_sign_up_label_is_visible()
        perform_login(self, email, password)
        self.main_page.check_logged_in_username(name)
        take_screenshot(self.page, 'valid_login')
        self.main_page.click_on_delete_account_button()
        self.account_deleted_page.account_deleted_message_is_visible()

    @pytest.mark.registration_and_login
    def test_invalid_login(self, test_setup):
        fake = Faker()
        self.main_page.check_main_page_is_opened()
        self.main_page.click_on_sign_up_login_button()
        self.sign_up_login_page.check_new_user_sign_up_label_is_visible()
        perform_login(self, fake.email(), fake.password())
        self.sign_up_login_page.check_error_message_is_visible()
        take_screenshot(self.page, 'invalid_login')

    @pytest.mark.registration_and_login
    def test_logout(self, test_setup):
        fake = Faker()
        self.main_page.check_main_page_is_opened()
        self.main_page.click_on_sign_up_login_button()
        email = fake.email()
        password = fake.password()
        name = fake.first_name()
        register_new_user(self, email, password, name)
        self.main_page.click_on_logout_button()
        self.sign_up_login_page.check_new_user_sign_up_label_is_visible()
        perform_login(self, email, password)
        self.main_page.check_logged_in_username(name)
        self.main_page.click_on_logout_button()
        self.sign_up_login_page.check_new_user_sign_up_label_is_visible()
        take_screenshot(self.page, 'logout')
        perform_login(self, email, password)
        self.main_page.check_logged_in_username(name)
        self.main_page.click_on_delete_account_button()
        self.account_deleted_page.account_deleted_message_is_visible()

    @pytest.mark.registration_and_login
    def test_register_with_existing_email(self, test_setup):
        fake = Faker()
        self.main_page.check_main_page_is_opened()
        self.main_page.click_on_sign_up_login_button()
        email = fake.email()
        password = fake.password()
        name = fake.first_name()
        register_new_user(self, email, password, name)
        self.main_page.click_on_logout_button()
        self.sign_up_login_page.check_new_user_sign_up_label_is_visible()
        self.main_page.click_on_sign_up_login_button()
        self.sign_up_login_page.check_new_user_sign_up_label_is_visible()
        self.sign_up_login_page.enter_name(fake.first_name())
        self.sign_up_login_page.enter_email(email)
        self.sign_up_login_page.click_on_sign_up_button()
        self.sign_up_login_page.check_email_error_message_is_visible()
        take_screenshot(self.page, 'existing_email_error')
        perform_login(self, email, password)
        self.main_page.check_logged_in_username(name)
        self.main_page.click_on_delete_account_button()
        self.account_deleted_page.account_deleted_message_is_visible()

    @pytest.mark.other_pages
    def test_contact_us_form(self, test_setup):
        self.main_page.check_main_page_is_opened()
        self.main_page.click_on_contact_us_button()
        self.contact_us_page.get_in_touch_is_visible()
        self.contact_us_page.enter_valid_get_in_touch_data()
        self.contact_us_page.upload_file()
        self.contact_us_page.click_on_submit_button()
        self.contact_us_page.success_message_is_visible()
        take_screenshot(self.page, 'contact_us_form')

    @pytest.mark.other_pages
    def test_test_cases_page(self, test_setup):
        self.main_page.check_main_page_is_opened()
        self.main_page.click_on_test_cases_button()
        self.test_cases_page.check_test_cases_label_is_visible()
        take_screenshot(self.page, 'test_cases_page')

    @pytest.mark.other_pages
    def test_all_products_and_product_detail_page(self, test_setup):
        self.main_page.check_main_page_is_opened()
        self.main_page.click_on_products_button()
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
        take_screenshot(self.page, 'product_details_visible')

    @pytest.mark.other_pages
    def test_search_product(self, test_setup):
        searched_product = 'Winter Top'
        self.main_page.check_main_page_is_opened()
        self.main_page.click_on_products_button()
        self.products_page.check_all_products_title_is_visible()
        self.products_page.enter_product_name_in_search_field(searched_product)
        self.products_page.click_on_search_button()
        self.products_page.check_found_product_is_visible(searched_product)
        take_screenshot(self.page, 'search_product')

    @pytest.mark.other_pages
    def test_subscription_in_home_page(self, test_setup):
        self.main_page.check_main_page_is_opened()
        self.main_page.check_subscription_text_is_visible()
        self.main_page.enter_email_in_your_email_address_field('qwerty@email.com')
        self.main_page.click_on_subscribe_button()
        self.main_page.success_message_is_visible('You have been successfully subscribed!')
        take_screenshot(self.page, 'subscription_home_page')

    @pytest.mark.cart
    def test_subscription_in_cart_page(self, test_setup):
        self.main_page.check_main_page_is_opened()
        self.main_page.click_on_cart_button()
        self.cart_page.shopping_cart_text_is_visible()
        self.main_page.check_subscription_text_is_visible()
        self.main_page.enter_email_in_your_email_address_field('qwerty@email.com')
        self.main_page.click_on_subscribe_button()
        self.main_page.success_message_is_visible('You have been successfully subscribed!')
        take_screenshot(self.page, 'subscription_cart_page')

    @pytest.mark.cart
    def test_adding_products_in_cart(self, test_setup):
        self.main_page.check_main_page_is_opened()
        self.main_page.click_on_products_button()
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
        self.cart_page.check_product_quantity("0", "1")
        self.cart_page.check_product_quantity("1", "1")
        self.cart_page.check_product_price("0", top_price)
        self.cart_page.check_product_price("1", tshirt_price)
        take_screenshot(self.page, 'add_prodcuts_to_cart')

    @pytest.mark.cart
    def test_product_quantity_in_cart(self, test_setup):
        self.main_page.check_main_page_is_opened()
        self.main_page.click_on_view_product_button()
        self.product_detail_page.check_product_name_is_visible()
        quantity = '4'
        self.product_detail_page.enter_quantity(quantity)
        self.product_detail_page.click_on_add_to_cart_button()
        self.product_detail_page.success_message_is_visible()
        self.product_detail_page.click_on_view_cart_button()
        self.cart_page.check_product_quantity("0", quantity)
        take_screenshot(self.page, 'quantity_in_cart')

    @pytest.mark.registration_and_login
    def test_register_while_checkout(self, test_setup):
        self.main_page.check_main_page_is_opened()
        self.main_page.add_product_to_cart()
        self.main_page.click_on_view_cart_link()
        self.cart_page.shopping_cart_text_is_visible()
        self.cart_page.click_on_proceed_to_checkout_button()
        self.cart_page.checkout_message_is_visible()
        self.cart_page.click_on_register_login_link()
        register_new_random_user(self)
        self.main_page.click_on_cart_button()
        self.cart_page.click_on_proceed_to_checkout_button()
        checkout_products(self)
        take_screenshot(self.page, 'register_while_checkout')
        self.order_placed_page.click_on_delete_account_button()
        self.account_deleted_page.account_deleted_message_is_visible()

    @pytest.mark.registration_and_login
    def test_register_before_checkout(self, test_setup):
        self.main_page.check_main_page_is_opened()
        self.main_page.click_on_sign_up_login_button()
        register_new_random_user(self)
        self.main_page.add_product_to_cart()
        self.main_page.click_on_view_cart_link()
        self.cart_page.shopping_cart_text_is_visible()
        self.cart_page.click_on_proceed_to_checkout_button()
        checkout_products(self)
        take_screenshot(self.page, 'registered_before_checkout')
        self.order_placed_page.click_on_delete_account_button()
        self.account_deleted_page.account_deleted_message_is_visible()
