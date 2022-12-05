import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    # btn1.click()

    btn = browser.find_element(By.ID,"book")
    btn.click()
    
    value_x = browser.find_element(By.ID, 'input_value').text
    x = calc(value_x)

    input = browser.find_element(By.ID, 'answer').send_keys(x)

    submit = browser.find_element(By.ID, 'solve').click()


finally:

    time.sleep(30)
    browser.quit()