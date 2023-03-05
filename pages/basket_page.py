from .base_page import BasePage
from .locators import BasketPageLocators
class BasketPage(BasePage):
    def should_not_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.NOT_EMPTY_BASKET), "Success message is presented, but should not be"

    def should_be_empty_messsage(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), "Empty message is not presented"