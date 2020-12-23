from time import sleep

from selenium import webdriver


class TestForm():
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def testcase2(self):
        '''
        打开testhome地址
        输入用户名
        输入密码
        记住用户
        点击登录
        :return:
        '''
        self.driver.get("https://testerhome.com/account/sign_in")
        self.driver.find_element_by_id('user_login').send_keys('webagent')
        self.driver.find_element_by_id('user_password').send_keys('adb server')
        self.driver.find_element_by_id('user_remember_me').click()
        self.driver.find_element_by_name('commit').click()
        sleep(5)