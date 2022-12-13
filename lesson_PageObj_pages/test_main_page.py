from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb"
    page = MainPage(browser, link)
    page.open()
    page.guest_clik_button_see_basket()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.check_availiable_goods_in_busket()

@pytest.mark.login_guest
class TestLoginFromMainPage():

# def go_to_login_page(browser):
#     login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
#     login_link.click()

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/" 
        page = MainPage(browser, link)
        page.open()
        # page.go_to_login_page()
        # page.should_be_login_link()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        # реализация теста
        link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = MainPage(browser, link) 
        page.open()
        page.go_to_login_page()




