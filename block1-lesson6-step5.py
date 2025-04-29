from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/find_link_text"

# driver_Chrome = webdriver.Chrome()
# driver_Firefox = webdriver.Firefox()
driver = webdriver.Chrome()

try:
    driver.get(link)

    link = driver.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link.click()


    input1 = driver.find_element(By.TAG_NAME, "input")
    input1.send_keys("Anya")
    input2 = driver.find_element(By.NAME, "last_name")
    input2.send_keys("Arlanova")
    input3 = driver.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Perm")
    input4 = driver.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    # После выполнения всех действий мы должны не забыть закрыть окно браузера
    driver.quit()