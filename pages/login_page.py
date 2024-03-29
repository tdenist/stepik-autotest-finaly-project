import time
from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        current_url = self.browser.current_url
        assert current_url.find("login") != -1 , "Current url is not login page url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"
		
    def register_new_user(self, email, password): # регистрация нового пользователя
        #self.go_to_login_page() # переходим на страницу логина
        self.browser.find_element(*LoginPageLocators.EMAIL_FILD).send_keys(email) # вводим e-mail
        self.browser.find_element(*LoginPageLocators.PASS_FILD).send_keys(password) # вводим пароль
        self.browser.find_element(*LoginPageLocators.PASS_FILD).send_keys(psssword) # повторяем ввод пароля
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click() # нажимаем кнопку регистрации