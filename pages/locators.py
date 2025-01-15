from selenium.webdriver.common.by import By


class BasePageLocators():
    # Эти ссылки есть на каждой из страниц сайта, поэтому решено вынести их отдельно
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    # Этот локатор нужен для проверки текста об ошибке
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")





class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    # локатор кнопки добавления товара в корзину
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")

    # локатор ожидаемого названия книги
    EXPECTED_NAME_OF_BOOK = (By.CSS_SELECTOR, "h1")

    # локатор ожидаемой цены книги
    EXPECTED_PRICE_OF_BOOK = (By.CSS_SELECTOR, "p.price_color")

    # локатор сообщения о том, что книга добавлена в корзину
    MESSAGE_BOOK_IN_BASKET = (By.CSS_SELECTOR, "div.alert:nth-child(1) .alertinner")

    # локатор сообщения стоимости всех добавленных товаров
    MESSAGE_PRICE_OF_BASKET = (By.CSS_SELECTOR, "div.alert:nth-child(3) .alertinner p")

    # локатор названия книги
    ACTUAL_NAME_OF_BOOK = (By.CSS_SELECTOR, "div.alert:nth-child(1) .alertinner strong")

    # локатор стоимости корзины
    ACTUAL_PRICE_OF_BOOK = (By.CSS_SELECTOR, "div.alert:nth-child(3) .alertinner p strong")



