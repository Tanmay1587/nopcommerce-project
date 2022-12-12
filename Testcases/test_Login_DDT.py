import time

import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from utilities import XLUtils

class Test_001_login:

    baseURL = ReadConfig.getAppURL()
    # path = ".//TestData/LoginData.xlsx"
    path = r'C:\Users\Tanmay.Gupta\PycharmProjects\nopcommerce\TestData\LoginData.xlsx'

    logger = LogGen.loggen()

    # def test_homePage(self,setup):
    #
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     act_Title = self.driver.title
    #     if act_Title == "Your store. Login":
    #         self.driver.close()
    #         assert True
    #     else:
    #         self.driver.save_screenshot(".\\Screenshots\\"+"test_homepage_title.png")
    #         self.driver.close()
    #         assert False

    def test_login(self,setup):
        self.logger.info("-------------------Testcase1 started-------------------")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        list_status = [] # Empty list variable
        self.rows = XLUtils.getRowCount(self.path,'sheet1')
        self.column = XLUtils.getColumnCount(self.path, 'sheet1')
        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, 'sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'sheet1', r, 3)
            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)
            act_title = self.driver.title

            if act_title == "Dashboard / nopCommerce administration":
                if self.exp == "Pass":
                    self.logger.info("-------------------Test Assertion Passed-------------------")
                    list_status.append("PASS")
                    self.lp.clickLogout()
                elif self.exp == "Fail":
                    self.logger.info("Testcase failed")
                    list.append("FAIL")
            else:
                if self.exp=='Pass':
                    self.logger.error("-------------------Assertion failure-------------------")
                    list.append("FAIL")
                elif self.exp=='Fail':
                    self.logger.info("Passed-----------------")
                    list_status.append("PASS")

        if "FAIL" not in list_status:
            self.logger.info("DDT Testcase is pass----------------------")
            self.driver.close()
            assert True
        else:
            self.logger.info("DDT Testcase is failed--------------------")
            self.driver.close()
            assert False

        self.logger.info("------------Testcase is completed")