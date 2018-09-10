import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



from selenium.webdriver.support.ui import WebDriverWait

class CommonLibrayDriverCreation(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.amazon.in")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
        unittest.main()
