from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import json
import re
import pytest
import unittest
from LIB.test_CommonLibraryDriverCreation import test_CommonLibraryDriverCreation
from BIN.GenricUiFunction import GenericUIFunction

with open("C:\Api_Automation\Python_Automation_Framework\CONFIG\commonconfig.json","r") as f:
    config_json = json.load(f)

class Dropdown(test_CommonLibraryDriverCreation,unittest.TestCase,GenericUIFunction):

    @pytest.mark.skip("Dont want to execute")
    def test_dropdown_landingpage(self):
        self.login_Amazon()
        self.WaitUntilElementFound(config_json["XPATH"]["shopbycataegoryelem"])
        self.mouse_over(config_json["XPATH"]["shopbycataegoryelem"])
        value = self.get_dropdown_values(config_json["XPATH"]["dropdwonlandingpage_count"],config_json["XPATH"]["dropdwonlandingpage_increment"])
        print value
        return value

    @pytest.mark.skip("Dont want to execute")
    def test_dropdown_yourorders(self):
        self.login_Amazon()
        self.WaitUntilElementFound(config_json["XPATH"]["yourorderelem"])
        self.mouse_over(config_json["XPATH"]["yourorderelem"])
        value = self.get_dropdown_values(config_json["XPATH"]["yourorders_count"],config_json["XPATH"]["yourorders_increment"])
        print value
        return value

    def test_click_signout(self):
        self.login_Amazon()
        self.WaitUntilElementFound(config_json["XPATH"]["yourorderelem"])
        self.mouse_over(config_json["XPATH"]["yourorderelem"])
        self.click_specific_dropdown_value(config_json["XPATH"]["yourorders_count"],config_json["XPATH"]["yourorders_increment"],"Sign Out")



if __name__ == "__main__":
    unittest.main()




