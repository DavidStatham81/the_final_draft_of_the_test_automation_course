from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import math
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators

class BasePage():
    # Конструктор — метод, который вызывается, когда мы создаем объект.
    # Конструктор объявляется ключевым словом __init__.
    # В него в качестве параметров мы передаем экземпляр драйвера и url адрес,
    # а так же время неявного ожидания элемента.
    # Внутри конструктора сохраняем эти данные как аттрибуты нашего класса.
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # Открываем страницу в браузере
    def open(self):
        self.browser.get(self.url)

    # Проверка того, что элемент отображается на странице
    # (будет ждать в соответствии с заданным неявным ожиданием 10 секунд)
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    # Проверка того, что элемент не появляется на странице в течение заданного времени:
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    # Проверка того, что элемент перестает отображаться на странице после истечения заданного времени
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    # Метод для расчета результата математического выражения
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        time.sleep(5)
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
            time.sleep(5)
        except NoAlertPresentException:
            print("No second alert presented")

    # Метод для проверки переходя на страницу автоирзации
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    # Метод для проверки наличия ссылки на страницу автоирзации
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
