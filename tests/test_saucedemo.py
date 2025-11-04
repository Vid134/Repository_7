from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_title_of_application():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)
    assert driver.title == "Swag Labs"
    driver.quit()

def test_homepage_url():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)
    assert driver.current_url == "https://www.saucedemo.com/"
    driver.quit()

def test_dashboard_url_after_login():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)
    assert "/inventory.html" in driver.current_url
    driver.quit()
