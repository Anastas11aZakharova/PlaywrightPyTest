from playwright.sync_api import Page, expect


class Products():
    def __init__(self, page: Page):
        self.page = page

        self.__all_products_title = self.page.locator('h2[class="title text-center"]')
        self.__all_products_list = self.page.locator('div[class="features_items"]')
        self.__blue_top_view_product = self.page.locator('a[href="/product_details/1"]')
        self.__search_field = self.page.locator('input[id="search_product"]')
        self.__search_button = self.page.locator('button[id="submit_search"]')
        self.__found_product = self.page.locator('//div[@class=\'productinfo text-center\']')
        self.__added_message = self.page.get_by_text('Your product has been added to cart.')
        self.__continue_shopping_button = self.page.locator('button[class="btn btn-success close-modal btn-block"]')
        self.__view_cart_link = self.page.locator('//a[@href=\'/view_cart\']').locator("nth=1")
        self.__product_info = self.page.locator('div[class="productinfo text-center"]')

    def check_all_products_title_is_visible(self) -> None:
        self.__all_products_title.wait_for(state='visible')
        expect(self.__all_products_title).to_be_visible()

    def check_all_products_list_is_visible(self) -> None:
        self.__all_products_list.wait_for(state='visible')
        expect(self.__all_products_list).to_be_visible()

    def click_on_blue_top_view_product(self) -> None:
        self.__blue_top_view_product.click()

    def enter_product_name_in_search_field(self, product_name) -> None:
        self.__search_field.fill(product_name)

    def click_on_search_button(self) -> None:
        self.__search_button.click()

    def check_found_product_is_visible(self, product_name) -> None:
        found_product = self.__found_product.locator("xpath=/p[text()='" + product_name + "']")
        expect(found_product).to_be_visible()

    def check_added_message_is_visible(self) -> None:
        self.__added_message.wait_for(state='visible')
        expect(self.__added_message).to_be_visible()

    def click_on_continue_shopping_button(self) -> None:
        self.__continue_shopping_button.click()

    def click_on_view_cart_link(self) -> None:
        self.__view_cart_link.click()

    def add_product_to_cart(self, product_name) -> None:
        self.__product_info.get_by_text(product_name).locator("xpath=/following-sibling::a").click()

    def get_product_price(self, product_name):
        return self.__product_info.get_by_text(product_name).locator("xpath=/preceding-sibling::h2").text_content()
