from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Firefox()
    browser.get(link)

    first_name = browser.find_element(By.CSS_SELECTOR, "form div.first_block div.form-group input.form-control.first")
    first_name.send_keys("Anya")

    last_name = browser.find_element(By.CSS_SELECTOR, "form div.first_block div.form-group input.form-control.second")
    last_name.send_keys("Arlanova")

    email = browser.find_element(By.CSS_SELECTOR, "form div.first_block div.form-group input.form-control.third")
    email.send_keys("a.arlanova@yandex.ru")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()