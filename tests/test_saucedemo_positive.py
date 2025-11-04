##Firstly Import modules from selenium and python
from selenium import webdriver  ##import webdriver to control the browser
from selenium.webdriver.common.by import By   ###By class helps in locating web elements on a webpage
import time                           ##Used to add pause where needed

## Testcase1 for validating title of application
def test_title_of_application():      ##is a pytest testcase function
    driver = webdriver.Chrome()   ##to launch chrome browser
    driver.get("https://www.saucedemo.com/")   ##to Open Website sauce-demo
    time.sleep(2)       ##to pause execution for 2secs
    assert driver.title == "Swag Labs"    ##assertion to verify that url contains domain name
    driver.quit()  ##to close browser after test execution

# Testcase2 for validating homepage url after succesful login
def test_homepage_url():    ###is a pytest testcase function
    driver = webdriver.Chrome()  ##to launch chrome browser
    driver.get("https://www.saucedemo.com/")     ##to Open Website sauce-demo
    time.sleep(2)               ##to pause execution for 2secs
    assert driver.current_url == "https://www.saucedemo.com/"    ##assertion to verify that url contain domain name
    driver.quit()        ##to close browser after test execution

# Testcase3 for validating dashboard url after succesful login
def test_dashboard_url_after_login():     #is a pytest testcase function
    driver = webdriver.Chrome()     ##to launch chrome browser
    driver.get("https://www.saucedemo.com/")     ##to Open Website sauce-demo
    driver.find_element(By.ID, "user-name").send_keys("standard_user")   #giving proper login credentials
    driver.find_element(By.ID, "password").send_keys("secret_sauce")    #giving proper login credentials
    driver.find_element(By.ID, "login-button").click()        #clicking the login button
    time.sleep(3)         ##to pause execution for 2secs
    assert "/inventory.html" in driver.current_url    ##assertion to verify that url contain inventory html shows succesful login
    driver.quit()        ##to close browser after test execution
