import json
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode for Jenkins
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

def test_login(driver):
    # Load login data
    with open('login.json', 'r') as file:
        data = json.load(file)
        app = data["apps"][0]

    driver.get(app["url"])

    wait = WebDriverWait(driver, 10)

    try:
        username_field = wait.until(EC.presence_of_element_located((By.ID, app["field"])))
        username_field.send_keys(app["value"])
    except TimeoutException:
        pytest.fail(f"Login field '{app['field']}' not found within timeout.")

    try:
        password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))
        password_field.send_keys(app["password"])
    except TimeoutException:
        pytest.fail("Password field not found within timeout.")

    try:
        login_button = wait.until(EC.element_to_be_clickable((By.ID, "Login")))
        login_button.click()
    except TimeoutException:
        pytest.fail("Login button not clickable within timeout.")

    # Validate login
    try:
        wait.until(EC.presence_of_element_located((By.ID, "homePageBody")))  # Example locator
        print("Login successful!")
    except TimeoutException:
        pytest.fail("Login failed or home page not loaded.")
