from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Step 1: Initialize WebDriver
driver = webdriver.Chrome(service=Service())

# Step 2: Open Website
driver.get("https://www.saucedemo.com/")
time.sleep(2)

# Step 3: Enter login credentials and login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(3)

# ✅ Step 4: Extract webpage HTML content
page_content = driver.page_source

# ✅ Step 5: Save to Text file
with open("Webpage_task_11.txt", "w", encoding="utf-8") as file:
    file.write(page_content)

print("✅ Webpage contents saved successfully as Webpage_task_11.txt")

# Step 6: Close browser
driver.quit()
