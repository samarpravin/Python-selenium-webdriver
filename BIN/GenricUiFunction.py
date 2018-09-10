from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class GenricUiFuncation:
    def clickelement(self,locator):
        ClickElement=self.driver.find_element_by_xpath(locator)
        ClickElement.click()

    def waitunitilelementfound(self,locator):
        timeout = 10
        element_present = EC.presence_of_element_located((By.XPATH, locator))
        WebDriverWait(self.driver, timeout).until(element_present)

    def inputelement(self,locator,input):
        timeout = 10
        email = self.driver.find_element_by_xpath(locator)
        email.send_keys(input)

    def gettextuielement(self,locator):
        landingpage = self.driver.find_element_by_xpath(locator)
        welcometxt = landingpage.text
        print welcometxt
        return(welcometxt)
