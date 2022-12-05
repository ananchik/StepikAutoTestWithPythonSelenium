import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import unittest

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"

        browser = webdriver.Chrome()
        browser.get(link)

        ###
        input_first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .first_class .first").send_keys("Ivak")
        input_last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .second_class .second").send_keys("Ivak")
        input_email = browser.find_element(By.CSS_SELECTOR, ".first_block .third_class .third").send_keys("Ivak")

        input_phone = browser.find_element(By.CSS_SELECTOR, ".second_block .first_class .first").send_keys("+7838383838")
        input_adress = browser.find_element(By.CSS_SELECTOR, ".second_block .second_class .second").send_keys("MSK")

        submit = browser.find_element(By.TAG_NAME, "button").click()
        ###

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "False with Congratulations in test 1")
        
    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"

        browser = webdriver.Chrome()
        browser.get(link)

            
        ###
        input_first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .first_class .first").send_keys("Ivak")
        input_last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .second_class .second").send_keys("Ivak")
        input_email = browser.find_element(By.CSS_SELECTOR, ".first_block .third_class .third").send_keys("Ivak")

        input_phone = browser.find_element(By.CSS_SELECTOR, ".second_block .first_class .first").send_keys("+7838383838")
        input_adress = browser.find_element(By.CSS_SELECTOR, ".second_block .second_class .second").send_keys("MSK")

        submit = browser.find_element(By.TAG_NAME, "button").click()
        ###
        
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "False with Congratulations in test 2")



if __name__ == "__main__":
    unittest.main()