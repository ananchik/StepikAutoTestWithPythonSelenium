from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = " http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    valuex = browser.find_element(By.ID, 'treasure')
    x = valuex.get_attribute('valuex')

    # x_element = browser.find_element(By.CSS_SELECTOR, '.form-group #input_value')
    # x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, ".form-group #answer")
    input1.send_keys(y)

    option = browser.find_element(By.ID, 'robotCheckbox')
    option.click()

    robot_btn = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    robot_btn.click()

    submit = browser.find_element(By.CLASS_NAME, 'btn')
    submit.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()