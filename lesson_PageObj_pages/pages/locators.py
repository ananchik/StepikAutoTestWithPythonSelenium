from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    EMAIL_VALUE = (By.CSS_SELECTOR, "#id_registration-email")
    PSWD1_VALUE = (By.CSS_SELECTOR, "#id_registration-password1")
    PSWD2_VALUE = (By.CSS_SELECTOR, "#id_registration-password2")

# class MainPageLocators():
#     LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    FORM_REGISTRATION = (By.CSS_SELECTOR, "#register_form")
    FORM_LOGIN = (By.CSS_SELECTOR, "#login_form")
    BUTTON_REGISTRATION = (By.CSS_SELECTOR, ".register_form .btn.btn-lg.btn-primary" )

class AddProductToBusketLocators():
    BUTTON_ADD_TO_BUSKET = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket") 
    INITIAL_BOOK_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    INITIAL_BOOK_PRICE = (By.CSS_SELECTOR,".alert.alert-safe.alert-noicon.alert-info.fade.in .alertinner  strong")
    NAME_AFTER_ADD_BOOK_TO_ADD = (By.CSS_SELECTOR,"#messages .alert.alert-safe.alert-noicon.alert-success.fade.in .alertinner  strong")

class AdditionToBusketForm():
    ADDITION_FORM_TO_BUSKET = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success.fade.in")

class ShowYourBusket():
    BTN_SHOW_BUSKET = (By.CSS_SELECTOR, ".btn-group .btn.btn-default")
    ITEMS_IN_BUSKET = (By.CSS_SELECTOR, ".basket-items")
    CONTENT_OF_BUSKET = (By.CSS_SELECTOR, "#content_inner p")