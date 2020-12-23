
from time import sleep

from selenium import webdriver
from selenium.webdriver import TouchActions


class TestTouchAction():
    def setup(self):
        #self.driver=webdriver.Chrome()
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option('w3c',False)
        self.driver=webdriver.Chrome(chrome_options=opt)
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def testcase1(self):
        """
        打开Chrome
        打开URL：http://www.baidu.com
        向搜索框中输入’selenium测试‘
        通过TouchAction点击搜索框
        滑动到底部，点击下一页
        关闭Chrome
        """
        self.driver.get("http://www.baidu.com")
        el=self.driver.find_element_by_id('kw')
        el.send_keys("selenium测试")
        el_search=self.driver.find_element_by_id('su')
        action=TouchActions(self.driver)
        action.tap(el_search)
        action.perform()
        action.scroll_from_element(el,0,10000).perform()
        #self.driver.find_element_by_css_selector('#page > div > a:nth-child(12)')
        self.driver.find_element_by_class_name('n').click()
        sleep(3)

