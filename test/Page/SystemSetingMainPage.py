#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @Site: 
# @File: SystemSetingMainPage.py.py
# @Author: JasonWu
# @E-mail: 15000257149@163.com
# @Time: 5月 08, 2020
# ---

from selenium.webdriver.common.by import By
from Page.system_seting.system_application_page import ApplicationPage
from Page.system_seting.system_voice_page import VoicePage
from Page.base_page import BasePage
import allure


class SystemSetingMainPage(BasePage):

    _voice_locator = (
        By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
                  ".widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget"
                  ".LinearLayout/android.widget.ListView/android.widget.LinearLayout[3] ")

    _application_locator = (
        By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
                  ".widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                  "/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget"
                  ".ListView/android.widget.LinearLayout[4]")

    def to_voice(self):
        allure.epic('SystemSeting')
        allure.feature('VoicePage')
        self.find_element(self._voice_locator).click()
        self.logger.info('_voice_locator点击成功')
        return VoicePage(self.driver)

    def to_application(self):
        allure.epic('SystemSeting')
        allure.feature('Application')
        self.driver.swipe(30, 1475, 30, 671, 300)
        self.find_element_and_click(self._application_locator)
        self.logger.info('_application_locator点击成功')
        return ApplicationPage(self.driver)
