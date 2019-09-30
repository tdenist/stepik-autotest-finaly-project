from pages.main_page import MainPage
from pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_can_go_to_login_page(browser):
    #link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы - переходим на страницу логина)
    login_page = LoginPage(browser, browser.current_url) #инициализируем LoginPage в теле теста
    login_page.should_be_login_page() # проверяем страницу логина

def test_guest_should_see_login_link(browser):
    #link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.should_be_login_link()      # проверяем наличие ссылки на страницу логина