import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#DRIVER
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(5)

class FindLink(unittest.TestCase):
    """Open the Nav Canada Page and find a link by the name of 'The Future'"""
    def setUp(self):
        self.driver = driver
        
    def test_link(self):
        self.driver.get("https://www.navcanada.ca/en/")
        web_dev_link = self.driver.find_elements(By.PARTIAL_LINK_TEXT, 'The Future')
        self.assertIsNotNone(web_dev_link)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
   unittest.main()
