from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class SIMA:
    def __init__(self):
        return self

    def Trask(self,a):
        titles = WebDriverWait(self.driver, 10).until(
           EC.presence_of_element_located((By.XPATH, a)))
        titles.click()
