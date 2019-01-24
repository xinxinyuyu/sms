# -*- coding: utf-8 -*-
import page
from base.base_action import BaseAction


class SettingPage(BaseAction):
    def __init__(self,driver):
        BaseAction.__init__(self,driver)

    # 1.点击搜索按钮
    def click_search_btn(self):
        self.click_element(page.setting_search_btn)

    # 2.输入搜索内容
    def input_edit_input_content(self,content):
        self.input_edit_content(page.setting_search_edit,content)

    # 3.点击返回
    def click_back_btn(self):
        self.click_element(page.setting_back_btn)



