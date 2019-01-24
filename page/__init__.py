# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
# 包名和启动名
setting_app_package = 'com.android.settings'
setting_app_activity = '.Settings'



# 搜索按钮
setting_search_btn = By.ID,"com.android.settings:id/search"
# 搜索框
setting_search_edit = By.ID,"android:id/search_src_text"
# 返回按钮
setting_back_btn = By.CLASS_NAME,"android.widget.ImageButton"