import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = " http://SunInJuly.github.io/execute_script.html"

    browser = webdriver.Chrome()
    browser.get(link)

    x_value = browser.find_element(By.ID, "input_value").text
    x = calc(x_value)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(x)

    check_box = browser.find_element(By.ID, "robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", check_box)
    check_box.click()
    
    robot_check = browser.find_element(By.ID, "robotsRule")
    robot_check.click()

    submit = browser.find_element(By.TAG_NAME, 'button')
    submit.click()

finally:

    time.sleep(30) 
    # закрываем браузер после всех манипуляций
    browser.quit()