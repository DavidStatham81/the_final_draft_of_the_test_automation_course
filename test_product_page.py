from .pages.product_page import ProductPage
import pytest
import time
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage


# Параметризация для этого теста закомментирована, для ускорения ревью
# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

# Проверка добавления товара в корзину, сравнение названия и стоимости товара в корзине и на карточке товара
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    name_product = page.message_product_added_to_basket()
    page.comparison_of_product_names(name_product)
    price_product = page.message_basket_price()
    page.comparison_product_price(price_product)


# Проверка отсутствия сообщения об успешном добавлении товара (после добавления товара)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


# Проверка отсутствия сообщения об успешном добавлении товара (после открытия страницы)
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


# Проверка того, что сообщение об успешном добавлении товара перестает отображаться на странице
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_disappear_of_success_message()


#  Проверка того, на странице товара есть ссылка на страницу авторизации
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


# Проверка того, на странице товара есть ссылка на страницу авторизации
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


# Проверка того, что со страницы товара гость может перейти в корзину, и проверить, что в ней нет товара
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_product()
    basket_page.should_be_empty_message()

# Проверка добавления товара в корзину, сравнение названия и стоимости товара в корзине и на карточке товара
# И
# Проверка отсутствия сообщения об успешном добавлении товара (после добавления товара)
# объединены в класс, для проверки работы функции setup
class TestUserAddToBasketFromProductPage(object):
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # Переход на страницу регистрации
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        # Регистрация нового пользователя
        email = str(time.time()) + "@fakemail.org"
        password = "TestPassword123"
        page.register_new_user(email, password)
        # Проверка, что пользователь залогинен
        page.should_be_authorized_user()

    # Проверка добавления товара в корзину, сравнение названия и стоимости товара в корзине и на карточке товара
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    # Проверка отсутствия сообщения об успешном добавлении товара (после добавления товара)
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        name_product = page.message_product_added_to_basket()
        page.comparison_of_product_names(name_product)
        price_product = page.message_basket_price()
        page.comparison_product_price(price_product)


