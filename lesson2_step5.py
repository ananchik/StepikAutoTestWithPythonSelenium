from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os

try:

    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]').send_keys("Ivan")
    last_name = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]').send_keys("Kukusha")
    email = browser.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys("aaa@mail.ru")


    current_dir = os.path.abspath(os.path.dirname(__file__)) 
    file_path = os.path.join(current_dir, 'file.txt')  
    file_download = browser.find_element(By.ID, "file")
    file_download.send_keys(file_path)

    submit = browser.find_element(By.TAG_NAME, 'button').click()


finally:
    time.sleep(30)
    browser.quit()
