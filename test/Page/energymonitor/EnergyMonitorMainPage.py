# coding=utf-8

"""
author: MiaZhang
Created on 2020/9/16 14:03
"""
import allure
from selenium.webdriver.common.by import By

from Page.base_page import BasePage


class EnergyMonitorMainPage(BasePage):
    _el1 = (By.XPATH,
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.Button")
    _el2 = (By.ID, "com.hryt.energymonitor:id/imb_show_route")
    _el3 = (By.ID, "com.hryt.energymonitor:id/bt_reset_a")
    _el4 = (By.ID, "com.hryt.energymonitor:id/imb_edit_route_a_name")
    _el5 = (By.ID, "com.hryt.energymonitor:id/hh_et")
    _el6 = (By.ID, "com.hryt.energymonitor:id/rl_bg")
    _el7 = (By.ID, "com.hryt.energymonitor:id/btn_navigationbar_back")
    _el8 = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.Button")

    def switch_travel_statistics_page(self):
        self.find_element(self._el2).click()
        self.logger.info('进入行程统计页面成功')
        self.find_element(self._el3).click()
        self.logger.info('点击重置按钮成功')
        self.find_element(self._el4).click()
        self.logger.info('点击行程A的修改按钮成功')
        self.element_send_keys(self._el5, '11311')
        self.logger.info('输入框中输入：11311')
        self.find_element(self._el6).click()
        self.logger.info('点击确定按钮，修改行程名称')
        self.find_element(self._el7).click()
        self.logger.info('点击返回，页面回到主页面')
        return self

    def switch_historical_power_consumption_page(self):
        self.find_element(self._el1).click()
        self.logger.info('进入历史电耗页面')
        return self

    def switch_instant_power_consumption_page(self):
        self.find_element(self._el8).click()
        self.logger.info('进入即可电耗页面成功')
        return self
