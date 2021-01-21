#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @Site: 
# @File: wait_tool.py
# @Author: JasonWu
# @E-mail: 15000257149@163.com
# @Time: 5月 08, 2020
# ---


#自定义逻辑条件
def loaded(self, driver):
    if len(self.driver.find_elements_by_id("someting")) >= 1:
        self.driver.find_elements_by_id("sometings").click
        return True
    else:
        return False