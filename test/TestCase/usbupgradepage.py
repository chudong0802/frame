# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @Site:
# @Author: JasonWu
# @E-mail: 15000257149@163.com
# @Time: 6月 30, 2020
# ---

import pytest
from selenium.webdriver.common.by import By
from Page.base_page import BasePage


class TestUsbUpGradePage(BasePage):
    _yestoup = (
        By.ID, "com.example.hyan6.pma_upgrade_app:id/update_Yes_btn")


    def test_to_upgrade(self):
        self.find_element(self._yestoup).click()

