import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig

class Test_001_login:

    baseURL = ReadConfig.getAppURL()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()

    def test_homePage(self,setup):

        self.driver = setup
        self.driver.get(self.baseURL)
        act_Title = self.driver.title
        if act_Title == "Your store. Login":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homepage_title.png")
            self.driver.close()
            assert False

    def test_login(self,setup):
        self.logger.info("-------------------Testcase1 started-------------------")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title

        if act_title == "Dashboard":
            self.driver.close()
            self.logger.info("-------------------Assertion Passed-------------------")
            assert True

        else:
            self.driver.close()
            self.logger.error("-------------------Assertion failure-------------------")
            assert False
