from selenium import webdriver
from selenium.webdriver.common.by import By
from base2.LoginPage import LoginPage
import unittest
import os


class LoginTests(unittest.TestCase):

    def test_validLogin(self):

        baseURL = "https://stportal.victorops.com/membership/#/"
        driverLocation = "/Users/bolof/Documents/selenium/base/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation

        driver = webdriver.Chrome(driverLocation)
        # driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        lp = LoginPage(driver)
        lp.login("bolo", "2k19")

        result = lp.verifyLoginSuccessful()
        assert result == True
        driver.quit()
