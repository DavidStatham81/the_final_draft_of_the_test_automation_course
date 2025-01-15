from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    # агрегируем все три метода в один, для облегчения написания теста
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    # проверяем, что текущая ссылка браузера - страница авторизации и регистрации
    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert "login" in current_url, f"Подстрока 'login' не найдена в URL: {current_url}"

    # Проверяем, что на странице есть форма входа
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    # Проверяем, что на странице есть форма регистрации
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"