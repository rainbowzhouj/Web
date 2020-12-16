import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://search.data4industry.com/")
        # 隐式等待
        self.driver.implicitly_wait(3)

    def test_wait(self):
        self.driver.find_element_by_class_name("searchBox").send_keys("化工原料")
        # self.driver.find_element_by_xpath('//*[@id="view"]/div/div[2]/div/div[2]/div[2]/button').click()
        self.driver.find_element_by_css_selector(
            "#view > div > div.content.clearfix > div > div:nth-child(3) > div.app-search.app-search-future > button").click()
        # 强制等待
        time.sleep(3)
        # print("hello")
        # def wait(x):
        #   return len(self.driver.find_element_by_xpath('//*[@id="view"]/div/div/div[1]/div/ul/li[2]'))>=1
        # 显示等待
        # WebDriverWait(self.driver, 5).until(
        #     expected_conditions.element_to_be_clickable('//*[@id="appList"]/li[2]/div/h4/a/span'))
        self.driver.find_element_by_css_selector( "#appList > li.list-item.dot-1 > div > h4 > a > span").click()

    def teardown(self):
        self.driver.quit()
