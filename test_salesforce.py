import json
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login(driver):
    with open('login.json', 'r') as file:
        data = json.load(file)
        apps = data["apps"]
        app = apps[0]

    driver.get(app["url"])
    time.sleep(2)

    try:
        driver.find_element(By.ID, app["field"]).send_keys(app["value"])
    except NoSuchElementException:
        pytest.fail(f"Login field '{app['field']}' not found.")

    try:
        driver.find_element(By.ID, "password").send_keys(app["password"])
    except NoSuchElementException:
        pytest.fail("Password field not found.")

    try:
        driver.find_element(By.ID, "Login").click()
    except NoSuchElementException:
        pytest.fail("Login button not found.")

    time.sleep(5)
