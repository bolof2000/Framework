from selenium.webdriver.common.by import By
# from base.selenium_driver import SeleniumDriver
from base2.TestBase import SeleniumDriver


class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    _email_field = "username"
    _password_field = "password"
    _login_button = "ext--login-submit"
    _verify_login = "Create Incident"

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="id")

    def login(self, email, password):

        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()