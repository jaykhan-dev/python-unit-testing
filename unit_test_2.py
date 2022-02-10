import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(5)

class SearchEnginesTest(unittest.TestCase):
    def test_Google(self):
        self.driver = driver
        self.driver.get("https://www.google.com/")
        print("Title of the page is: " + self.driver.title)
    
    def test_Bing(self):
        self.driver = driver
        self.driver.get("https://bing.com")
        print("Title of the page is: " + self.driver.title)
        
if __name__ == "__main__":
    unittest.main()