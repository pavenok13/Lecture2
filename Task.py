import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from DAVE import SAME
from X_PATH import SIMA

class Search(unittest.TestCase):
        def setUp(self):
            self.driver = webdriver.Chrome('chromedriver.exe')
            self.driver.get('http://www.google.com/ncr')

        def test_search(self):
            driver = self.driver
            assert 'Google' in self.driver.title
            element = self.driver.find_element_by_name("q")
            element.send_keys('selenide')
            element.send_keys(Keys.RETURN)
            SAME.Fact(self)
            assert 'https://ru.selenide.org/' in self.driver.current_url
            Url = driver.current_url
            driver.back()
            assert 'Google' in self.driver.title
            a = '//*[@id="hdtb-msb-vis"]/div[4]/a'
            SIMA.Trask(self,a)
            a = '//*[@id="islrg"]/div/div/a/div/img'
            SIMA.Trask(self, a)
            picture = self.driver.find_element_by_class_name('pM4Snf')
            assert 'ru.selenide.org' in picture.text
            All = self.driver.find_element_by_class_name('NZmxZe')
            All.click()
            SAME.Fact(self)
            assert Url in driver.current_url



        def tearDown(self):
            self.driver.close()

if __name__ == '__main__':
    unittest.main()