from selenium import webdriver
from selenium.webdriver.common.by import By
import time

BASE_URL = "https://www.saucedemo.com/"
ERROR_SELECTOR = "h3[data-test='error']"  # Error message element

def test_login_wrong_password():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)

    # Enter valid username but wrong password
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("wrong_pass")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(10)

    error = driver.find_element(By.CSS_SELECTOR, ERROR_SELECTOR).text
    assert "Username and password do not match" in error


    driver.quit()


def test_login_wrong_username():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)

    driver.find_element(By.ID, "user-name").send_keys("incorrect_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(10)

    error = driver.find_element(By.CSS_SELECTOR, ERROR_SELECTOR).text
    assert "Username and password do not match" in error

    driver.quit()


def test_locked_out_user_error_message():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)

    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(5)

    error = driver.find_element(By.CSS_SELECTOR, ERROR_SELECTOR).text

    assert "Sorry, this user has been locked out" in error

    driver.quit()