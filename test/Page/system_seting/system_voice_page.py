#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @Site: 
# @File: system_voice_page.py
# @Author: JasonWu
# @E-mail: 15000257149@163.com
# @Time: 5月 08, 2020
# ---
from selenium.webdriver.common.by import By
from Page.base_page import BasePage


class VoicePage(BasePage):
    _switch_button = (By.ID, "switch_button")

    def search(self):
        self.find_element_and_click(self._switch_button)
        self.logger.info('_switch_button点击成功')
        return self

    def xpath(self, xpathid):
        self.driver.find_element_by_xpath(xpathid).click()
        self.logger.info(xpathid + '点击成功')
        return self

    def get_text(self):
        text = self.find_element(self._switch_button)
        self.logger.info('_switch_button定位成功')
        return text.get_attribute("text")
