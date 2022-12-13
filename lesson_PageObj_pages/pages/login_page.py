from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in str(self.url), "Word 'login' is not in URL"
        # assert True

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.FORM_LOGIN), "There is not Login Form"
        # assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        # assert True
        assert self.is_element_present(*LoginPageLocators.FORM_REGISTRATION), "There is not Registration Form"

    def register_new_user(self, email, password):
        # email = str(time.time()) + "@fakemail.org"
        # password = "WWW123$$$"
        # self.go_to_login_page()

        email_for_filling, psswd1_for_filling, psswd2_for_filling = self.fill_in_email_and_password_in_reg_form()
        email_for_filling.send_keys(email)
        psswd1_for_filling.send_keys(password)
        psswd2_for_filling.send_keys(password)

        self.should_registrate_new_user()