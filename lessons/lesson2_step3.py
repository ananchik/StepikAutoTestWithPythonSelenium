from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try: 
    link = "https://suninjuly.github.io/selects1.html"

    browser = webdriver.Chrome()
    browser.get(link)


    first_num = int(browser.find_element(By.ID, "num1").text)
    second_num = int(browser.find_element(By.ID, "num2").text)
    total = first_num + second_num
    print(total)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(f'{total}') # ищем элемент с текстом "Python"

    submit = browser.find_element(By.CLASS_NAME, 'btn')
    submit.click()
    

finally:

    time.sleep(30) 
    # закрываем браузер после всех манипуляций
    browser.quit()