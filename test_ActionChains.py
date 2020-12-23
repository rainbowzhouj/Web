from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    @pytest.mark.skip
    def testcase(self):
        elemenet_click = self.driver.find_element_by_xpath("//input[@value='click me']")
        elemenet_doubleclick = self.driver.find_element_by_xpath("//input[@value='dbl click me']")
        elemenet_rightclick = self.driver.find_element_by_xpath("//input[@value='right click me']")
        action = ActionChains(self.driver)
        action.click(elemenet_click)
        action.context_click(elemenet_rightclick)
        action.double_click(elemenet_doubleclick)
        action.perform()

    # 将鼠标移动到某个元素上
    def test_movetoelement(self):
        self.driver.get("https://www.baidu.com")
        eles = self.driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')
        #eles = self.driver.find_element_by_css_selector('#s-usersetting-top')
        #eles = self.driver.find_element_by_partial_link_text('设置')
        action = ActionChains(self.driver)
        action.move_to_element(eles)
        action.perform()
        sleep(3)

    # 将鼠标托动到某个元素上
    def test_dragelement(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        # 自定义方式：按住
        drag_element = self.driver.find_element_by_id("dragger")
        # 自定义方式：拖动
        drop_element = self.driver.find_element_by_xpath("/html/body/div[2]")
        action = ActionChains(self.driver)
        # action.drag_and_drop(drag_element,drop_element).perform()
        # 自带函数方式
        #action.click_and_hold(drag_element).release(drop_element).perform()
        action.click_and_hold(drag_element).move_to_element(drop_element).release().perform()
        sleep(3)

    # 模拟按键方法，
    '''
    1、win32 api实现
    2、Sendkey来实现
    3、selenium的WebElement对象send_ken()方法来实现
    
    - Action=ActionChains(driver)
    - action_send_keys(Keys.Back_SPACE)
    - action_key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL)
    - action.perform()
    '''
    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele=self.driver.find_element_by_xpath('/html/body/label[1]/input')
        ele.click()
        action=ActionChains(self.driver)
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("TOM").pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()
        sleep(3)



    def teardown(self):
        self.driver.quit()
