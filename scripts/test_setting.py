# -*- coding: utf-8 -*-
import os,sys
sys.path.append(os.getcwd())
from base.read_data import read_yaml_data


import time
import pytest

import page
from base.init_driver import get_driver
from page.setting_page import SettingPage

#读取sms_send.yaml的数据
def get_data():
    data = read_yaml_data("search_data.yaml")
    return data.get("setting_data")

class TestSetting:
    def setup_class(self):
        self.driver = get_driver(page.setting_app_package,page.setting_app_activity)
        self.setting_page = SettingPage(self.driver)

    def teardown_class(self):
        time.sleep(1)
        self.driver.quit()

    # 点击搜索按钮
    def test_click_search(self):
        self.setting_page.click_search_btn()

    @pytest.mark.parametrize("content",get_data())
    # 输入框输入内容(输入1之后再输入2会自动覆盖1)
    def test_input_edit_in_content(self,content):
        self.setting_page.input_edit_input_content(content)

    # 点击返回按钮
    def test_click_back(self):
        self.setting_page.click_back_btn()
