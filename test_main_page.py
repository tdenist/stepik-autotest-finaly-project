from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_basket_page()         # выполняем метод страницы - переходим на страницу корзины        
    basket_page = BasketPage(browser, browser.current_url)    # инициализируем BasketPage в теле теста
    basket_page.should_not_be_product_in_basket()    # проверяем, что в корзине нет товаров
    basket_page.should_be_message_basket_is_empty()  # проверяем что есть текст о том, что корзина пуста 
	
@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                      # открываем страницу
        page.go_to_login_page()          # выполняем метод страницы - переходим на страницу логина)
        login_page = LoginPage(browser, browser.current_url) # инициализируем LoginPage в теле теста
        login_page.should_be_login_page() # проверяем страницу логина
		
    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                      # открываем страницу
        page.should_be_login_link()      # проверяем наличие ссылки на страницу логина