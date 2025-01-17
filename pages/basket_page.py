from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    # Проверка того, что в корзине нет товаров
    def should_not_be_product(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_NOT_EMPTY), \
            "The basket is not empty!"

    # Проверка того, что есть текст о том что корзина пуста
    def should_be_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_BASKET_EMPTY), \
            "There is no message that the basket is empty!"
