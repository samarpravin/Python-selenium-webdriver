import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from LIB.test_CommonLibraryDriverCreation import CommonLibrayDriverCreation
from BIN.GenricUiFunction import GenricUiFuncation
from selenium.webdriver.support.ui import WebDriverWait

class test_login_amazon_TC01(CommonLibrayDriverCreation,unittest.TestCase,GenricUiFuncation):


    def test_Amazon_search(self):
        self.test_login_functionality()
        self.waitunitilelementfound('//div[@class="nav-search-field "]/label/following-sibling::input[@id="twotabsearchtextbox"]')
        self.inputelement('//div[@class="nav-search-field "]/label/following-sibling::input[@id="twotabsearchtextbox"]','TV')
        self.clickelement('//input[@type="submit"]')


if __name__ == "__main__":
    unittest.main()