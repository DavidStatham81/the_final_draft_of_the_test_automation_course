from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        print("Trying to find the add to basket button")
        button_add = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        print("Button found")
        button_add.click()
        print("Button clicked")
        self.solve_quiz_and_get_code()
