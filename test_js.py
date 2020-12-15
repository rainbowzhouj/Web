import time

import pytest

from base import Base


class TestJS(Base):
    @pytest.mark.skip
    def test_js_scroll(self):
        self.driver.get("htttps://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("selenium test")
        element=self.driver.execute_script("return document.getElementById('su')")
        element.click()
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='page']/a[10]").click()
        time.sleep(3)
        for code in [
            'return document.title','return JSON.stringify(performance.timing)'
        ]:
            print(self.drive.execute_script(code))


    def test_datetime(self):
        self.driver.get("")
        time_element = self.driver.execute_script("a = document.getElementById('train_date');a.removeAttribute('readonly')")
        self.driver.execute_script("document.getElementById('train_date').value='2020-12-30'")
        time.sleep(3)
        print(self.driver.execute_script("return document.getElementById('train_date').value"))