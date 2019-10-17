from pages.basket_page import BasketPage
from pages.product_page import ProductPage
from pages.login_page import LoginPage
import time
import pytest

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0"
@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link, 15)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.add_product_to_basket()     # нажимаем кнопку Добавить в корзину
    page.solve_quiz_and_get_code()   # ввод ответа на мат.выражение
    page.should_be_product_name_in_message_add_to_basket() # проверяем, что название товара в сообщении о добавлении товара, с тем, который добавили  
    page.should_be_product_price_in_message_add_to_basket() # проверяем, что в сообщении о стоимости корзины стоимость корзины совпадает с ценой товара

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
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link, 15)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы - переходим на страницу логина)
    login_page = LoginPage(browser, browser.current_url) #инициализируем LoginPage в теле теста
    login_page.should_be_login_page() # проверяем страницу логина

@pytest.mark.need_review    
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_basket_page()         # выполняем метод страницы - переходим на страницу корзины        
    basket_page = BasketPage(browser, browser.current_url)    # инициализируем BasketPage в теле теста
    basket_page.should_not_be_product_in_basket()    # проверяем, что в корзине нет товаров
    basket_page.should_be_message_basket_is_empty()  # проверяем что есть текст о том, что корзина пуста 

@pytest.mark.test_user_add_to_basket
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):   # регистрируем нового пользователя 
        page = LoginPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                      # открываем страницу
        #page.go_to_login_page()          # выполняем метод страницы - переходим на страницу логина)
        email = str(time.time()) + "@fakemail.org"
        page.register_new_user(email, "123qweASD") # регистрируем нового пользователя
        page.should_be_authorized_user() # проверяем, что пользователь зарегистрирован
    
    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link, 15)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                      # открываем страницу
        page.should_not_be_success_message()    # проверяем, что нет сообщения об успехе с помощью is_not_element_present
    
    @pytest.mark.need_review
    @pytest.mark.xfail
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link, 15)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                      # открываем страницу
        page.add_product_to_basket()     # нажимаем кнопку Добавить в корзину
        page.solve_quiz_and_get_code()   # ввод ответа на мат.выражение
        page.should_be_product_name_in_message_add_to_basket() # проверяем, что название товара в сообщении о добавлении товара, с тем, который добавили  
        page.should_be_product_price_in_message_add_to_basket() # проверяем, что в сообщении о стоимости корзины стоимость корзины совпадает с ценой товара
 