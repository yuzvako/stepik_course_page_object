from .base_page import BasePage
from .locators import ProductPageLocators
class ProductPage(BasePage):
    def all_defs(self):
        self.should_add_book_to_basket()
    def should_add_book_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()
        self.solve_quiz_and_get_code()
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Add to basket not found"