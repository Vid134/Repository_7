##Firstly Import modules from selenium and python
from selenium import webdriver   ###import webdriver to control the browser
from selenium.webdriver.common.by import By   ##By class helps in locating web elements on a webpage
import time       ##Used to add pause where needed

BASE_URL = "https://www.saucedemo.com/"    #to Open Website sauce-demo
ERROR_SELECTOR = "h3[data-test='error']"  # Error message element

##Test case 1 by giving wrong password
def test_login_wrong_password():
    driver = webdriver.Chrome()  ###to launch chrome browser
    driver.get(BASE_URL)    #to Open Website sauce-demo

    # Enter valid username but wrong password
    driver.find_element(By.ID, "user-name").send_keys("standard_user")    ##giving valid username
    driver.find_element(By.ID, "password").send_keys("wrong_pass")   #giving wrong_pass as password
    driver.find_element(By.ID, "login-button").click()  ##to click the login button
    time.sleep(10)   ##to pause execution for 10secs

    error = driver.find_element(By.CSS_SELECTOR, ERROR_SELECTOR).text    #error message element
    assert "Username and password do not match" in error  ##assertion shown username and password dont match


    driver.quit()     ##to close browser after test execution

##Test case 2 by giving wrong username
def test_login_wrong_username():
    driver = webdriver.Chrome()   ##to launch chrome browser
    driver.get(BASE_URL)   #to Open Website sauce-demo

    driver.find_element(By.ID, "user-name").send_keys("incorrect_user")  ##giving incorrect username
    driver.find_element(By.ID, "password").send_keys("secret_sauce")   ##giving correct pasword
    driver.find_element(By.ID, "login-button").click()     ##clicking the login button
    time.sleep(10)      ##to pause execution for 10secs

    error = driver.find_element(By.CSS_SELECTOR, ERROR_SELECTOR).text    #error message elemen
    assert "Username and password do not match" in error    ##assertion shown username and password dont match

    driver.quit()    ##to close browser after test execution


##Test case 3 to show locked out user on usernmae
def test_locked_out_user_error_message():
    driver = webdriver.Chrome()   ##to launch chrome browser
    driver.get(BASE_URL)       #to Open Website sauce-demo

    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")  #shows locked out user
    driver.find_element(By.ID, "password").send_keys("secret_sauce")   ## password as secret_sauce
    driver.find_element(By.ID, "login-button").click()  ##to click the login button
    time.sleep(5)     ##to pause execution for 5secs

    error = driver.find_element(By.CSS_SELECTOR, ERROR_SELECTOR).text   ## #error message elemen

    assert "Sorry, this user has been locked out" in error    ##assertion shown username and password dont match

    driver.quit()   ##to stop the browser