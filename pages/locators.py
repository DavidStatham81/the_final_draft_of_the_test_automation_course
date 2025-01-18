from selenium.webdriver.common.by import By


class BasePageLocators():
    # Эти ссылки есть на каждой из страниц сайта, поэтому решено вынести их отдельно
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    # Этот локатор нужен для проверки текста об ошибке
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    # Локатор для проверки того, что пользователь залогинен
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button:nth-child(7)")

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

class BasketPageLocators():
    # Локатор кнопки перехода в корзину
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > a:nth-child(1)")

    # Локатор указывающий на то, что корзине не пуста
    BASKET_NOT_EMPTY = (By.CSS_SELECTOR, "h2.col-sm-6")

    # Локатор сообщения о том, что в корзине нет товаров
    MESSAGE_BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner > p:nth-child(1)")



