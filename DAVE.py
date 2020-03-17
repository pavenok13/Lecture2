from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class SAME:
    def __init__(self):
        pass

    def Fact(self):
        titles = WebDriverWait(self.driver, 10).until(
           EC.presence_of_element_located((By.TAG_NAME, 'h3')))
        titles.click()