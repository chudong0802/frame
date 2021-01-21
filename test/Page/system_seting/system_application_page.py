#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @Site: 
# @File: system_application_page.py
# @Author: JasonWu
# @E-mail: 15000257149@163.com
# @Time: 5月 09, 2020
# ---
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

from Page.base_page import BasePage


class ApplicationPage(BasePage):
    _360locator = (By.ID, "switch_button")

    def click(self):
        self.find_element_and_click(self._360locator)
        self.logger.info('_360locator点击成功')
        return self
