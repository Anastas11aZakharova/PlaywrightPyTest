from faker import Faker


def register_new_user(page, email, password, first_name) -> None:
    fake = Faker()
    page.sign_up_login_page.check_new_user_sign_up_label_is_visible()
    page.sign_up_login_page.enter_name(first_name)
    page.sign_up_login_page.enter_email(email)
    page.sign_up_login_page.click_on_sign_up_button()
    page.enter_account_information_page.check_enter_account_information_label_is_visible()
    page.enter_account_information_page.enter_valid_data(password, fake.random_int(1, 28, 1), fake.month_name(),
                                                         fake.random_int(1980, 2021, 1),
                                                         first_name, fake.last_name(), fake.word(), fake.address(),
                                                         fake.address(), fake.current_country(), fake.state(),
                                                         fake.city(), fake.zipcode(), fake.random_number(9))
    page.account_created_page.account_created_mesage_is_visible()
    page.account_created_page.click_on_continue_button()
    page.main_page.check_logged_in_username(first_name)


def register_new_random_user(page) -> None:
    fake = Faker()
    register_new_user(page, fake.email(), fake.password(), fake.first_name())


def checkout_products(page) -> None:
    fake = Faker()
    page.address_details_page.check_address_details_header_is_visible()
    page.address_details_page.check_review_your_order_header_is_visible()
    page.address_details_page.enter_text_in_text_area(fake.word())
    page.address_details_page.click_on_place_order_button()
    page.payment_page.check_payment_header_is_visible()
    page.payment_page.check_payment_fields_are_visible()
    page.payment_page.enter_valid_payment_data()
    page.payment_page.click_pay_and_confirm_button()
    page.order_placed_page.check_success_message_is_visible()


def perform_login(page, login, password) -> None:
    page.sign_up_login_page.enter_login_email(login)
    page.sign_up_login_page.enter_login_password(password)
    page.sign_up_login_page.click_on_login_button()
