import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from LIB.CommonLibrayDriverCreation import CommonLibrayDriverCreation
from BIN.GenricUiFunction import GenricUiFuncation
from selenium.webdriver.support.ui import WebDriverWait

class test_login_amazon_TC01(CommonLibrayDriverCreation,unittest.TestCase,GenricUiFuncation):


    def test_login_functionality(self):
        ##timeout = 10
        self.driver.maximize_window()
        timeout = 10
        self.clickelement("//span[contains(text(),'Hello. Sign in')]")
        self.waitunitilelementfound("//input[@type='email']")
        self.inputelement('//input[@type="email"]','pravin.kusin@gmail.com')
        continuebutton=self.driver.find_element_by_xpath("//input[@id='continue']")
        continuebutton.click()
        element_present = EC.presence_of_element_located((By.XPATH, "//input[@id='ap_password']"))
        WebDriverWait(self.driver, timeout).until(element_present)
        #WebDriverWait(self.driver, timeout).until(element_present)
        password = self.driver.find_element_by_xpath("//input[@id='ap_password']")
        password.send_keys("Hari&sadu11")
        login = self.driver.find_element_by_xpath("//input[@id='signInSubmit']")
        login.click()
        element_present = EC.presence_of_element_located((By.XPATH, "//div[@id='nav-tools']/a[1]/span[@class='nav-line-1']"))
        WebDriverWait(self.driver, timeout).until(element_present)
        timeout = 10
        welcometxt=self.gettextuielement("//div[@id='nav-tools']/a[1]/span[@class='nav-line-1']")
        splitvar = welcometxt.split(",")
        if splitvar[0] == "Hello":
            print "login is successfull for the user {}".format(welcometxt)
        else:
            print "login is not successfull for the user {}".format(welcometxt)
            raise Exception
        ###samar
    def test_Amazon_search(self):
        self.test_login_functionality()
        self.waitunitilelementfound('//div[@class="nav-search-field "]/label/following-sibling::input[@id="twotabsearchtextbox"]')
        self.inputelement('//div[@class="nav-search-field "]/label/following-sibling::input[@id="twotabsearchtextbox"]','TV')
        self.clickelement('//input[@type="submit"]')


if __name__ == "__main__":
    unittest.main()