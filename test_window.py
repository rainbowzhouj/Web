from time import sleep

from selenium import webdriver

from base import Base
class TestWindows(Base):
    def test_window(self):
        '''
        打开百度页面
        点击登录
        弹框中点击立即注册，输入用户名喝账号
        返回刚才的登录也，点击登录
        输入用户名和密码，点击登录
        :return:
        '''
        self.driv
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_link_text("登录").click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        self.driver.find_element_by_link_text("立即注册").click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        windows=self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("username")
        self.driver.find_element_by_name("phone").send_keys("13452808722")
        self.driver.find_element_by_id("TANGRAM__PSP_4__password").send_keys("Touchchains")

        self.driver.switch_to.window(windows[0])
        #self.driver.find_element_by_class("tang-pass-footerBarQrcode pass-link").click()
        self.driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()
        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("username")
        self.driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys("ActionChains")
        self.driver.find_element_by_id("TANGRAM__PSP_11__submit").click()
        sleep(3)