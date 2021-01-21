#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @Site: 
# @File: data_config.py
# @Author: JasonWu
# @E-mail: 15000257149@163.com
# @Time: 5月 08, 2020
# ---
from appium.webdriver.webdriver import WebDriver
from conda_env.yaml import yaml


class DataConfig:
    def __init__(self, path):
        file = open(path, "r")
        self.steps = yaml.safe_load(file)

    def run(self, driver: WebDriver):
        for step in self.steps:
            element = None

            if isinstance(step, dict):
                if "id" in step.keys():
                    element = driver.find_element_by_id(step["id"])
                elif "xpath" in step.keys():
                    element = driver.find_element_by_xpath(step["xpath"])
                else:
                    print(step.keys())

                if "input" in step.keys():
                    element.send_keys(step["input"])
                else:
                    element.click()

                if "get" in step.keys():
                    text = element.get_attribute(step["get"])
                    return text