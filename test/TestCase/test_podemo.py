# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @Site: 
# @File: test_podemo.py
# @Author: JasonWu
# @E-mail: 15000257149@163.com
# @Time: 5月 08, 2020
# ---

import allure
from Drivers.systemseting_driver import systemseting_app


class TestDemo:
    def setup(self):
        self.system_voice_page = systemseting_app.start().to_voice()

    @allure.story('MuteButton')
    def test_po_demo(self):
        self.system_voice_page.search()
        assert "开启" in self.system_voice_page.get_text()

    def teardown(self):
        # os.system("adb reboot")
        systemseting_app.quit()
