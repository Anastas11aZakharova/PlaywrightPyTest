def register_new_random_user(page) -> None:
  
    page.sign_up_login_page.check_new_user_sign_up_label_is_visible()
    page.sign_up_login_page.enter_name("Thomas")
    page.sign_up_login_page.enter_email("thomas@email.com")
    page.sign_up_login_page.click_on_sign_up_button()
    page.enter_account_information_page.check_enter_account_information_label_is_visible()
    page.enter_account_information_page.enter_valid_data()
    page.account_created_page.account_created_mesage_is_visible()
    page.account_created_page.click_on_continue_button()
    page.main_page.check_logged_in_username('Thomas')

def checkout_products(page) -> None:
    page.address_details_page.check_address_details_header_is_visible()
    page.address_details_page.check_review_your_order_header_is_visible()
    page.address_details_page.enter_text_in_text_area('qwertyqwerty')
    page.address_details_page.click_on_place_order_button()
    page.payment_page.check_payment_header_is_visible()
    page.payment_page.check_payment_fields_are_visible()
    page.payment_page.enter_valid_payment_data()
    page.payment_page.click_pay_and_confirm_button()
    page.order_placed_page.check_success_message_is_visible()

def perform_login(page,login,password) -> None:
    page.sign_up_login_page.enter_login_email('thomas@email.com')
    page.sign_up_login_page.enter_login_password('asdfg')
    page.sign_up_login_page.click_on_login_button()
