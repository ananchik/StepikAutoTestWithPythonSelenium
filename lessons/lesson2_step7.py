import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, 'button').click()

    # new_window = browser.window_handles[1]
    # browser.switch_to.new_window(new_window)

    browser.switch_to.window(browser.window_handles[1])
    

    value_x = browser.find_element(By.ID, 'input_value').text
    x = calc(value_x)

    input = browser.find_element(By.ID, 'answer').send_keys(x)

    submit = browser.find_element(By.TAG_NAME, 'button').click()

finally:

    time.sleep(30)
    browser.quit()
