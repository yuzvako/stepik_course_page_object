from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()
        self.solve_quiz_and_get_code()
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Add to basket not found"

    def should_add_book_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()
        self.solve_quiz_and_get_code()
        self.should_book_name_equal()
        self.should_equal_book_and_basket()
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Add to basket not found"


    def should_book_name_equal(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        item_message = self.browser.find_element(*ProductPageLocators.MESSAGE_NAME_BOOK).text
        assert book_name == item_message, f"The book in card is not equal"

    def should_equal_book_and_basket(self):
        self.book_price = self.browser.find_element(*ProductPageLocators.PRICE_BOOK).text[1:]
        self.basket = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text[1:]
        assert self.book_price == self.basket, "Prices is not equal"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
