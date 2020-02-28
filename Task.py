import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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
            time.sleep(2)
            titles = self.driver.find_element_by_tag_name('h3')
            titles.click()
            assert 'https://ru.selenide.org/' in self.driver.current_url
            Url = driver.current_url
            driver.back()
            time.sleep(2)
            assert 'Google' in self.driver.title
            yet = self.driver.find_element_by_class_name('hdtb-dd-b')
            yet.click()
            time.sleep(2)
            images = self.driver.find_element_by_class_name('f9UGee')
            images.click()
            time.sleep(2)
            picture = self.driver.find_element_by_xpath('//*[@id="islrg"]/div/div/a/div/img')
            picture.click()
            time.sleep(2)
            picture = self.driver.find_element_by_class_name('pM4Snf')
            assert 'ru.selenide.org' in picture.text
            All = self.driver.find_element_by_class_name('NZmxZe')
            All.click()
            time.sleep(2)
            titles_2 = self.driver.find_element_by_tag_name('h3')
            titles_2.click()
            assert Url in driver.current_url



        def tearDown(self):
            self.driver.close()

if __name__ == '__main__':
    unittest.main()