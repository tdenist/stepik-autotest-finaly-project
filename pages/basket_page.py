from pages.base_page import BasePage
from pages.locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_product_in_basket(self):
	    assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), "Basket is not empty, products is in basket"

    def should_be_message_basket_is_empty(self):
	    assert self.is_element_present(*BasketPageLocators.MESSAGE_BASKET_IS_EMPTY), "Message - basket is empty - is not present"