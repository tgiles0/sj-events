from sj_events import constants
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class SeatJunky:
    def __init__(self, username, password, region):
        self.username = username
        self.password = password
        self.region = region
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--headless")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome("chromedriver", chrome_options=self.options)

    def do_user_login(self):
        self.driver.get(constants.SJ_LOGIN_PAGE.format(self.region))
        user_field = self.driver.find_element("id", constants.SJ_USER_FIELD)
        user_field.send_keys(self.username)
        pwd_field = self.driver.find_element("id", constants.SJ_PASSWORD_FIELD)
        pwd_field.send_keys(self.password)

        self.driver.find_element("name", constants.SJ_LOGIN_BUTTON).click()

        login_wait = WebDriverWait(driver=self.driver, timeout=10).until(
            lambda x: x.execute_script("return document.readyState === 'complete'")
        )

        errors = self.driver.find_elements(By.CLASS_NAME, constants.SJ_LOGIN_ERROR_CLASS)

        if any(constants.SJ_LOGIN_ERROR in e.text for e in errors):
            print("Error during login")
        else:
            print("Login successful")

