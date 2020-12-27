

'''
打开百度图片网址：https://image.baidu.com
识别上传按钮
点击上传按钮
将本地的图片文件上传
'''
import time

from base import Base


class TestFile(Base):
    def test_file_upload(self):
        self.driver.get("https://image.baidu.com")
        self.driver.find_element_by_xpath("//*[@id='sttb']/img[1]").click()
        self.driver.find_element_by_xpath('//*[@id="stfile"]').send_keys("C:\\Users\\10043\\PycharmProjects\\selenium\\Docker.jpg")
        time.sleep(7)