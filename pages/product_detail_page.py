from playwright.sync_api import Page, expect


class ProductDetail():
    def __init__(self, page: Page):
        self.page = page

        self.__write_your_review_bar =  self.page.get_by_text('Write Your Review')
        self.__product_name = self.page.locator('//div[@class=\'product-information\']/h2')
        self.__category =  self.page.locator('//div[@class=\'product-information\']/p[contains(text(),\'Category:\')]')
        self.__price =  self.page.locator('//div[@class=\'product-information\']//span[contains(text(),\'Rs. 500\')]')
        self.__availability =  self.page.locator('//div[@class=\'product-information\']//p//b[contains(text(),\'Availability:\')]/..')
        self.__condition =  self.page.locator('//div[@class=\'product-information\']//p//b[contains(text(),\'Condition:\')]/..')
        self.__brand =  self.page.locator('//div[@class=\'product-information\']//p//b[contains(text(),\'Brand:\')]/..')
        self.__product_quantity =  self.page.locator('input[id="quantity"]')
        self.__add_to_cart_button =  self.page.locator('button[class="btn btn-default cart"]')
        self.__success_message = self.page.get_by_text('Your product has been added to cart.')
        self.__view_cart_button = self.page.get_by_text('View Cart').locator("nth=0")


    def check_write_your_review_bar_is_visible(self) -> None:
        self.__write_your_review_bar.wait_for(state='visible')
        expect(self.__write_your_review_bar).to_be_visible()
    def check_product_name_is_visible(self) -> None:
        self.__product_name.wait_for(state='visible')
        expect(self.__product_name).to_be_visible()
    def check_category_is_visible(self) -> None:
        self.__category.wait_for(state='visible')
        expect(self.__category).to_be_visible()
    def check_price_is_visible(self) -> None:
        self.__price.wait_for(state='visible')
        expect(self.__price).to_be_visible()
    def check_availability_is_visible(self) -> None:
        self.__availability.wait_for(state='visible')
        expect(self.__availability).to_be_visible()
    def check_condition_is_visible(self) -> None:
        self.__condition.wait_for(state='visible')
        expect(self.__condition).to_be_visible()
    def check_brand_is_visible(self) -> None:
        self.__brand.wait_for(state='visible')
        expect(self.__brand).to_be_visible()
    def enter_quantity(self,quantity) -> None:
        self.__product_quantity.fill(quantity)
    def click_on_add_to_cart_button(self) -> None:
        self.__add_to_cart_button.click()
    def success_message_is_visible(self) -> None:
        self.__success_message.wait_for(state='visible')
        expect(self.__success_message).to_be_visible()
    def click_on_view_cart_button(self) -> None:
        self.__view_cart_button.click()



