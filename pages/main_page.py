from .base_page import BasePage
from .locators import MainPageLocators

# Заглушка. Метод __init__ вызывается при создании объекта
# Конструктор  с ключевым словом super  вызывает конструктор класса предка и передает
# ему все те аргументы, которые мы передали в конструктор MainPage.
class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)






