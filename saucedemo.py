##Firstly Import modules from selenium and python
from selenium import webdriver  #import webdriver to control the browser
from selenium.webdriver.chrome.service import Service   #service helps in initialising chrome driver
from selenium.webdriver.common.by import By   #By class helps in locating web elements on a webpage
import time           #Used to add pause where needed

##Initialize WebDriver or Launching the chrome web driver
driver = webdriver.Chrome(service=Service())

## Open Website sauce-demo
driver.get("https://www.saucedemo.com/")
time.sleep(2)  #to pause execution for 2secs

## Enter login credentials and login
driver.find_element(By.ID, "user-name").send_keys("standard_user")   #username=standard_user
driver.find_element(By.ID, "password").send_keys("secret_sauce")     #password=secret_sauce
driver.find_element(By.ID, "login-button").click()   #clicks the login button
time.sleep(3)   #to pause execution for 3secs

## Extract and print the current url
page_content = driver.page_source

## Saving the page content into a text file
with open("Webpage_task_11.txt", "w", encoding="utf-8") as file:
    file.write(page_content) ##this will write the content to a text file

print("Webpage contents saved successfully as Webpage_task_11.txt")  #page content saved succesfully as webpage_task_11.txt

## To Close browser
driver.quit()
