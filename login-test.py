from selenium import webdriver
from selenium.webdriver.common.by import By
from base2.LoginPage import LoginPage
import unittest
import os


class LoginTests(unittest.TestCase):

    def test_validLogin(self):
        # baseURL = "https://letskodeit.teachable.com/"
        baseURL = "https://stportal.victorops.com/membership/#/"
        driverLocation = "/Users/bolof/Documents/selenium/base/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation

        driver = webdriver.Chrome(driverLocation)
        # driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        lp = LoginPage(driver)
        lp.login("bolof2000", "Dammy2k100")

        userIcon = driver.find_element(By.LINK_TEXT, "Create Incident")
        if userIcon is not None:
            print("Login Successful")
        else:
            print("Login Failed")