import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")
        # 隐式等待
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def test_wait(self):
        #self.driver.find_element(By.CSS_SELECTOR,'#kw').send_keys("霍格沃兹测试学院")
        self.driver.find_element(By.CSS_SELECTOR,'[id=kw]').send_keys("Bigdata")
        self.driver.find_element(By.ID,'su').click()
        # 强制等待
        time.sleep(3)
        # print("hello")
        # def wait(x):
        #   return len(self.driver.find_element_by_xpath('//*[@id="view"]/div/div/div[1]/div/ul/li[2]'))>=1
        # 显示等待
        # WebDriverWait(self.driver, 5).until(
        #     expected_conditions.element_to_be_clickable('//*[@id="appList"]/li[2]/div/h4/a/span'))
        #self.driver.find_element_by_css_selector( "#appList > li.list-item.dot-1 > div > h4 > a > span").click()

    def teardown(self):
        self.driver.quit()
