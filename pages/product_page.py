from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    def add_product_to_basket(self): # нажимаем кнопку добавления товара в корзину
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        button_add_to_basket.click()

    def should_be_product_name_in_message_add_to_basket (self): # проверяем, что название товара в сообщении о добавлении товара, с тем, который добавили
        # проверяем наличие названия товара на странице
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented"
        # проверяем наличие сообщения о добавлении товара
        assert self.browser.find_element(*ProductPageLocators.MESSAGE_ADD_TO_BASKET), "Message add to basket is not presented"
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text
        assert product_name_in_message.find(product_name) != -1, "No product name in message add basket"

    def get_product_price(self): # метод возвращает цену продукта
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return product_name.text
	
    def should_be_product_price_in_message_add_to_basket (self): # проверяем, что в сообщении о стоимости корзины стоимость корзины совпадает с ценой товара
        # проверяем наличие цены товара на странице
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented"
        # проверяем наличие сообщения о стоимости корзины
        assert self.browser.find_element(*ProductPageLocators.MESSAGE_TOTAL_BASKET), "Message total basket is not presented"
        product_price_in_message = self.browser.find_element(*ProductPageLocators.MESSAGE_TOTAL_BASKET).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert product_price_in_message.find(product_price) != -1, "No product price in the message"