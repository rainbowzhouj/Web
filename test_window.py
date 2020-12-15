
from selenium import webdriver

class Test_Windows():
    def setup(self):
        self.driver=webdriver.chrome()
        self.driver.implictly_wait(5)
        self.driver.maxwindows()

    def teardown(self):
        self.driver.quite()