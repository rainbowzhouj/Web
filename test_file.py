

'''
打开百度图片网址：https://image.baidu.com
识别上传按钮
点击上传按钮
将本地的图片文件上传
'''
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base import Base


class TestFile(Base):
    def test_file_upload(self):
        self.driver.get("https://image.baidu.com")
        self.driver.find_element_by_xpath("//*[@id='sttb']/img[1]").click()
        #ID Name> CSS Selector > Xpath > Link > Class Name >Tag name
        self.driver.find_element_by_id('stfile').send_keys(r"C:\Users\10043\PycharmProjects\selenium\Docker.jpg")
        # 再次上传,name 定位
        self.driver.find_element_by_name('file').send_keys(r"C:\Users\10043\Pictures\virtual.PNG")
        # 再次上传，CSS Selector定位
        self.driver.find_element_by_css_selector('#app > div > div:nth-child(1) > div > div.graph-header-top > div > span > span.graph-searchnew-submit > span > div > form > input').send_keys(r"C:\Users\10043\Pictures\MongoDB.png")
        # 再次上传，Xpath定位
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/div/span/span[2]/span/div/form/input').send_keys("C:\\Users\\10043\\PycharmProjects\\selenium\\Docker.jpg")
        # 再次上传，Class Name定位
        self.driver.find_element_by_class_name('general-upload-file').send_keys(r"C:\Users\10043\Pictures\HBase-Hadoop.jpg")

