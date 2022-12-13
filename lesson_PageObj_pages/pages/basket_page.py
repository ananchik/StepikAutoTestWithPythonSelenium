from selenium.webdriver.common.by import By
from .base_page import BasePage 
from .locators import ShowYourBusket


class BasketPage(BasePage):

    def check_availiable_goods_in_busket(self):
        self.should_be_empty_basket()
        self.should_be_text_about_empty_basket()

    def should_be_empty_basket(self):
        assert self.is_element_present(*ShowYourBusket.ITEMS_IN_BUSKET) == False, "There are some goods in your basket"
        # assert self.browser.find_element(By.CSS_SELECTOR, ".basket-items")

    def should_be_text_about_empty_basket(self):
        assert self.browser.find_element(*ShowYourBusket.CONTENT_OF_BUSKET).text == "Your basket is empty. Continue shopping", "Your basket is not empty"
         
        

     
