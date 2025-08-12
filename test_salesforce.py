import json
import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Required for Jenkins
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login(driver):
    # Debugging info for Jenkins
    print("Python Version: ", os.sys.version)
    print("Working Directory: ", os.getcwd())
    print("Files in current directory: ", os.listdir())

    # Correct path to login.json
    json_path = os.path.join(os.path.dirname(__file__), 'login.json')
    if not os.path.exists(json_path):
        pytest.fail(f"login.json not found at {json_path}")

    # Load credentials
    with open(json_path, 'r') as file:
        data = json.load(file)
        apps = data["apps"]
        app = apps[0]

    # Open Salesforce login
    driver.get(app["url"])

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, app["field"]))
        ).send_keys(app["value"])
    except TimeoutException:
        pytest.fail(f"Login field '{app['field']}' not found.")

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "password"))
        ).send_keys(app["password"])
    except TimeoutException:
        pytest.fail("Password field not found.")

    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "Login"))
        ).click()
    except TimeoutException:
        pytest.fail("Login button not found.")

    # Wait for login success indicator
    try:
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "phSearchInput"))  # Search box in Salesforce
        )
        print("✅ Login successful.")
    except TimeoutException:
        pytest.fail("Login might have failed — search box not found.")
