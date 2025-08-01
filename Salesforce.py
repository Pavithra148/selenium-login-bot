import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

with open('login.json','r') as file:
    data = json.load(file)

    apps = data["apps"]

    app=apps[0]
# Loop through all apps


    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(app["url"])
    time.sleep(2)  

    try:
        # Fill the login field (email/username/user_id)
        driver.find_element(By.ID, app["field"]).send_keys(app["value"])
        print(f"Filled in {app['field']}")
    except NoSuchElementException:
        print(f"Login field '{app['field']}' not found in {app['name']}")
        driver.quit()
        exit()

    try:
        # Fill the password field
        driver.find_element(By.ID, "password").send_keys(app["password"])
    except NoSuchElementException:
        print("Password field not found.")
        driver.quit()
        exit()

    try:
        # Click login button
        driver.find_element(By.ID,"Login").click()
        print(f"Clicked login button for {app['name']}")
    except NoSuchElementException:
        print(f"Login button '{app['login_button']}' not found.")

    time.sleep(5) 
    driver.quit()
