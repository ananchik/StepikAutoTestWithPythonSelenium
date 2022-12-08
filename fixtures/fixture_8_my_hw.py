import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
import math
from selenium.webdriver.support.ui import WebDriverWait
import unittest


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    msg = ""
    links_list =  [
        "https://stepik.org/lesson/236895/step/1",
        "https://stepik.org/lesson/236896/step/1",
        "https://stepik.org/lesson/236897/step/1",
        "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236899/step/1",
        "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1",
        "https://stepik.org/lesson/236905/step/1"
    ]
    
    # -- let it be here
    # @pytest.mark.parametrize('links', links_list)
    # def test_guest_should_login(self, browser, links):
    #     link = links
    #     browser.get(link+"?auth=login")
    #     browser.implicitly_wait(15)

    #     login = browser.find_element(By.ID, "id_login_email").send_keys("")
    #     pswd = browser.find_element(By.ID, "id_login_password").send_keys("")
    #     enter_btn = browser.find_element(By.CSS_SELECTOR, ".sign-form__btn.button_with-loader ").click()


    @pytest.mark.parametrize('links', links_list)
    def test_guest_should_click(self, browser, links):
        link = links

        # Block of signing in 
        browser.get(link+"?auth=login")
        browser.implicitly_wait(15)
        time.sleep(5)
        page_login = browser.find_element(By.ID, "id_login_email")
        login = browser.find_element(By.ID, "id_login_email").send_keys("your_login")
        pswd = browser.find_element(By.ID, "id_login_password").send_keys("your_password")
        enter_btn = browser.find_element(By.CSS_SELECTOR, ".sign-form__btn.button_with-loader ").click()
        browser.implicitly_wait(30)
        
        # Block of real eximations
        browser.get(link)
        browser.implicitly_wait(15)
        browser.find_element(By.CSS_SELECTOR, ".textarea").send_keys(str(math.log(int(time.time()))))

        button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
        )
        button.click()

        # time.sleep(5)

        browser.implicitly_wait(15)

        message = WebDriverWait(browser, 20).until(
             EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
        ).text
        # print("ПЕРЕМЕННАЯ MESSAGE - ", message)
        # time.sleep(5)
        if message !="Correct!":
            self.msg += message
        print(self.msg)

        assert message == False



if __name__ == "__main__":
    unittest.main()
