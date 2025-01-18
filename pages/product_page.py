from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    # Клик по кнопке добавления товара в корзину, переход на алерт, подсчет кода,
    # переход на следующий алерт и его закрытие
    def add_to_basket(self):
        button_add = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add.click()
        # Прохождение капчи - только для акций, временно закомментирован
        # self.solve_quiz_and_get_code()

    # Поиск сообщения о том, что товар добавлен в корзину, возврат наименования товара.
    def message_product_added_to_basket(self):
        # Находим название добавляемого товара
        name_product = self.browser.find_element(*ProductPageLocators.EXPECTED_NAME_OF_BOOK).text
        return name_product

    # Сравнение наименования товара в сообщении и на карточке товара
    def comparison_of_product_names(self, name_product):
        # Находим название добавляемого товара
        product_name_from_the_message = self.browser.find_element(*ProductPageLocators.ACTUAL_NAME_OF_BOOK).text
        # Проверка того, что название товара в сообщении совпадает с названием товара, который действительно добавили.
        assert name_product == product_name_from_the_message, "Incorrect product added to cart"

    # Поиск сообщения со стоимостью корзины.
    def message_basket_price(self):
        # Находим стоимость добавляемого товара
        price_product = self.browser.find_element(*ProductPageLocators.EXPECTED_PRICE_OF_BOOK).text
        return price_product

    # Сравнение цены на карточке товара и стоимости корзины в сообщении
    def comparison_product_price(self, price_product):
        # Находим сообщение со стоимостью корзины.Стоимость корзины должна совпадать с ценой товара.
        price_product_in_message = self.browser.find_element(*ProductPageLocators.ACTUAL_PRICE_OF_BOOK).text
        # Сраванивем сообщения
        assert price_product == price_product_in_message, "The price of the product does not match"

    # Проверяем, что на странице отсутствует сообщение об успешном добавлении товара
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_BOOK_IN_BASKET), \
            "Success message is presented, but should not be"

    # Проверяем, что сообщение об успешном добавлении товара исчезло со страницы
    def should_disappear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_BOOK_IN_BASKET), \
            "Success message is presented, but should not be"

