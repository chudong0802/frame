# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @Site: 
# @File: test_podemo2.py
# @Author: JasonWu
# @E-mail: 15000257149@163.com
# @Time: 5月 09, 2020
# ---

from Drivers.systemseting_driver import systemseting_app


class TestDemo2:
    def setup(self):
        self.system_application_page = systemseting_app.start().to_application()

    def test_po_demo2(self):
        self.system_application_page.click()

    def teardown(self):
        # os.system("adb reboot")
        systemseting_app.quit()