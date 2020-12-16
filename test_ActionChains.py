from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains

class TestActionChains():
    def setup(self):
        self.driver=webdriver.Chrome()

    @pytest.mark.skip
    def testcase(self):
        elemenet_click=self.driver.find_element_by_xpath("//input[@value='click me']")
        elemenet_doubleclick=self.driver.find_element_by_xpath("//input[@value='dbl click me']")
        elemenet_rightclick = self.driver.find_element_by_xpath("//input[@value='right click me']")
        action=ActionChains(self.driver)
        action.click(elemenet_click)
        action.context_click(elemenet_rightclick)
        action.double_click(elemenet_doubleclick)
        action.perform()


    # 将鼠标移动到某个元素上
    def test_movetoelement(self):
        self.driver.get("https://www.baidu.com")
        ele=self.driver.find_element_by_link_text('设置')
        action=ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        sleep(3)

    # 将鼠标托动到某个元素上
    def test_dragelement(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        # 自定义方式：按住
        drag_element=self.driver.find_element_by_id("dragger")
        # 自定义方式：拖动
        drop_element=self.driver.find_element_by_xpath("/html/body/div[2]")
        action=ActionChains(self.driver)
        # action.drag_and_drop(drag_element,drop_element).perform()
        # 自带函数方式
        action.click_and_hold(drag_element).release(drop_element).perform()


    def teardown(self):
        self.driver.quit()