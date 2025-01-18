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

    # Метод для регистрации пользователя
    def register_new_user(self, email, password):
        # Ввод email
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        email_input.clear()
        email_input.send_keys(email)

        # Ввод пароля
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(password)

        # Ввод подтверждения пароля
        confirm_password_input = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_INPUT)
        confirm_password_input.clear()
        confirm_password_input.send_keys(password)

        # Нажатие кнопки регистрации
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()


