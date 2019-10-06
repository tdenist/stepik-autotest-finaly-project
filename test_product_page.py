from pages.main_page import MainPage
from pages.product_page import ProductPage
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link, 15)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.add_product_to_basket()     # нажимаем кнопку Добавить в корзину
    page.solve_quiz_and_get_code()   # ввод ответа на мат.выражение
    page.should_be_product_name_in_message_add_to_basket # проверяем, что название товара в сообщении о добавлении товара, с тем, который добавили  
    page.should_be_product_price_in_message_add_to_basket() # проверяем, что в сообщении о стоимости корзины стоимость корзины совпадает с ценой товара
    time.sleep(10)