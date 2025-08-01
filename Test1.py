from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Chrome
driver = webdriver.Chrome()

# Open website
driver.get("https://login.salesforce.com/")
driver.maximize_window()

driver.find_element(By.ID,"username").send_keys("pavithra.thangarasu14520@agentforce.com")
driver.find_element(By.ID,"password").send_keys("Pavithra@14")
driver.find_element(By.ID,"Login").click()
time.sleep(5)