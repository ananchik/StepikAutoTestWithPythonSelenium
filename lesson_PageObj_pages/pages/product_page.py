from selenium.webdriver.common.by import By
from .locators import AddProductToBusketLocators, AdditionToBusketForm
from .base_page import BasePage
# import time


class ProductPage(BasePage):

    def add_to_busket(self):
        btn_add_to_busket = self.browser.find_element(*AddProductToBusketLocators.BUTTON_ADD_TO_BUSKET)
        btn_add_to_busket.click() 
        # time.sleep(2)
        return self.solve_quiz_and_get_code()
        
        # alert = self.browser.switch_to.alert

    def check_book_name(self):
        print()
        initial_book_name = self.browser.find_element(*AddProductToBusketLocators.INITIAL_BOOK_NAME).text
        book_name_after_add_to_busket = self.browser.find_element(*AddProductToBusketLocators.NAME_AFTER_ADD_BOOK_TO_ADD).text
        # print("BOOK NAMES: ")
        # print("-", initial_book_name, "\n", "-", book_name_after_add_to_busket)
        assert  initial_book_name == book_name_after_add_to_busket, "BOOK NAMES ARE NOT THE SAME"

    def check_form_of_add_product_to_busket(self):
        assert self.is_not_element_present(*AdditionToBusketForm.ADDITION_FORM_TO_BUSKET), "Success message is presented, but should not be. Func is 'is_not_element_present'"

    def check_succes_message(self):
        assert self.is_disappeared(*AdditionToBusketForm.ADDITION_FORM_TO_BUSKET), "Disappear in 4s. Func is 'is_disappeared'"