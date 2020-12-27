import time

import pytest

from base import Base


class TestJS(Base):
    @pytest.mark.skip
    def test_js_scroll(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("selenium test")
        element=self.driver.execute_script("return document.getElementById('su')")
        element.click()
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        time.sleep(2)
        # 点击下一页
        self.driver.find_element_by_xpath("//*[@id='page']/div/a[10]").click()
        time.sleep(3)
        # 获取当前页的性能数据
        for code in [
            'return document.title','return JSON.stringify(performance.timing)'
        ]:
            print(self.driver.execute_script(code))

    #@pytest.mark.skip
    def test_datetime(self):
        '''
        要取消日期的readonly属性
        给value赋值
        写js代码来实现如上的1、2点，再webdriver对js进行处理
        :return:
        '''
        self.driver.get("https://www.12306.cn/index/")
        time_element = self.driver.execute_script("a = document.getElementById('train_date');a.removeAttribute('readonly')")
        self.driver.execute_script("document.getElementById('train_date').value='2020-12-30'")
        time.sleep(3)
        print(self.driver.execute_script("return document.getElementById('train_date').value"))

