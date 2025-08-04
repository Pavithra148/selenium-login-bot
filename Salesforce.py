import unittest
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import HtmlTestRunner

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_login(self):
        with open('login.json', 'r') as file:
            data = json.load(file)
            apps = data["apps"]
            app = apps[0]

            driver = self.driver
            driver.get(app["url"])
            time.sleep(2)

            try:
                driver.find_element(By.ID, app["field"]).send_keys(app["value"])
                print(f"Filled in {app['field']}")
            except NoSuchElementException:
                self.fail(f"Login field '{app['field']}' not found.")

            try:
                driver.find_element(By.ID, "password").send_keys(app["password"])
            except NoSuchElementException:
                self.fail("Password field not found.")

            try:
                driver.find_element(By.ID, "Login").click()
                print(f"Clicked login button for {app['name']}")
            except NoSuchElementException:
                self.fail(f"Login button not found for {app['name']}")

            time.sleep(5)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
      unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output='deployment/reports',
            report_name='report', 
            report_title='Salesforce Login Test Report',
            combine_reports=True,
            add_timestamp=True     
        )
    )
