from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Chrome
driver = webdriver.Chrome()

# Open website
driver.get("https://example.com")
driver.maximize_window()

# Interact with elements (dummy IDs for demo)
driver.find_element(By.ID, "username").send_keys("testuser")
driver.find_element(By.ID, "password").send_keys("testpass")
driver.find_element(By.ID, "login").click()

# Wait and quit
time.sleep(3)
driver.quit()
