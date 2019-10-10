from pages.main_page import MainPage
from pages.product_page import ProductPage
import time
import pytest

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0"

@pytest.mark.xfail
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link, 15)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.add_product_to_basket()     # нажимаем кнопку Добавить в корзину
    page.solve_quiz_and_get_code()   # ввод ответа на мат.выражение
    page.should_be_product_name_in_message_add_to_basket() # проверяем, что название товара в сообщении о добавлении товара, с тем, который добавили  
    page.should_be_product_price_in_message_add_to_basket() # проверяем, что в сообщении о стоимости корзины стоимость корзины совпадает с ценой товара
    #time.sleep(10)

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link, 15)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.add_product_to_basket()     # нажимаем кнопку Добавить в корзину
    page.solve_quiz_and_get_code()   # ввод ответа на мат.выражение    
    page.should_not_be_success_message()    # проверяем, что нет сообщения об успехе с помощью is_not_element_present

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link, 15)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.should_not_be_success_message()    # проверяем, что нет сообщения об успехе с помощью is_not_element_present

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link, 15)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.add_product_to_basket()     # нажимаем кнопку Добавить в 
    page.solve_quiz_and_get_code()   # ввод ответа на мат.выражение
    time.sleep(1)
    page.should_disapper_success_message()    # Проверяем, что нет сообщения об успехе с помощью is_disappeared

def test_guest_should_see_login_link_on_product_page(browser):
    #link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    #link = "http://selenium1py.pythonanywhere.com/"
    page = ProductPage(browser, link, 15)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы - переходим на страницу логина)
    login_page = LoginPage(browser, browser.current_url) #инициализируем LoginPage в теле теста
    login_page.should_be_login_page() # проверяем страницу логина