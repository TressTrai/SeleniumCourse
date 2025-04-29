from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

from selenium.webdriver.support.wait import WebDriverWait


try:
    link = "https://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, "button")
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button.click()

    x = int(browser.find_element(By.ID, "input_value").text)
    y = math.log(abs(12 * math.sin(x)), math.e)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    browser.find_element(By.ID, "solve").click()

finally:
    time.sleep(5)
    browser.quit()