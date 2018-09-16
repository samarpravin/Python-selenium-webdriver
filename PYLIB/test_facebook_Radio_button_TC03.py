from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import json
import re
import unittest
from LIB.test_CommonLibraryDriverCreation import test_CommonLibraryDriverCreation
from BIN.GenricUiFunction import GenericUIFunction
import os
import time

fileDir = os.path.dirname(os.path.realpath('__file__'))
print fileDir
filename = os.path.join(fileDir, '../CONFIG/commonconfig.json')
with open(filename,"r") as f:
    config_json = json.load(f)

class test_login_facebeook(test_CommonLibraryDriverCreation,unittest.TestCase,GenericUIFunction):
    def test_login_facebeook(self):
        self.driver.maximize_window()
        self.InputElement(config_json["XPATHFB"]["firstname"],"samar")
        self.InputElement(config_json["XPATHFB"]["lastname"],"jeet")
        self.InputElement(config_json["XPATHFB"]["registration"],"8754388083")
        self.InputElement(config_json["XPATHFB"]["newpassword"],"bbth")
        # day=Select(self.driver.find_element_by_xpath("//select[@name='birthday_day']"))
        # day.select_by_visible_text("25")
        # day = Select(self.driver.find_element_by_xpath("//select[@name='birthday_month']"))
        # day.select_by_visible_text("Oct")
        # day = Select(self.driver.find_element_by_xpath("//select[@name='birthday_year']"))
        # day.select_by_visible_text("2011")
        # self.ClickElement("//input[@type='radio']/following-sibling::label[contains(text(),'Male')]")
        self.SelectElement(config_json["XPATHFB"]["birthday"],"26")
        self.SelectElement(config_json["XPATHFB"]["birthmonth"],"Oct")
        self.SelectElement(config_json["XPATHFB"]["birthyear"],"2010")
        self.ClickElement(config_json["XPATHFB"]["Gender"])
        time.sleep(30)


if __name__ == "__main__":
    unittest.main()