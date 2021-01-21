#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @Site: 
# @File: demo_alpha.py
# @Author: JasonWu
# @E-mail: 15000257149@163.com
# @Time: 4月 30, 2020
# ---
from time import sleep

import pytest as pytest
from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from conda_env.yaml import yaml

from Page.system_seting.system_voice_page import VoicePage


class TestDemo_alpha:
    search_data = yaml.safe_load(open("../Data/search_data.yaml", "r"))  # 参数化引用
    print(search_data)

    def setup(self):
        caps = {}
        caps["autoGrantPermissions"] = True
        caps["platformName"] = "android"
        caps["deviceName"] = "whatever"
        caps["appActivity"] = ".MainActivity"
        caps["appPackage"] = "com.hryt.systemsettingshmi"
        caps["unicodeKeyboard"] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    @pytest.mark.parametrize("button", search_data)  # 参数化
    def test_demo2(self, button):
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[3]"
        ).click()
        # 低级Xpath定位（脆弱），因为attribute属性不全
        # self.driver.find_element_by_xpath("//*[text='someting' and contains(@resource-id, 'someting') ]").click()
        # 高级Xpath定位（健壮），理想状态，需要Android开发将每个Button组件定义独立的resource-id等属性
        self.driver.find_element_by_id(button).click()
        text = self.driver.find_element_by_id("switch_button")
        assert "开启" in text.get_attribute("text")
        # assert len(self.driver.find_elements_by_xpath(
        #     "//*[@text= '开启' and contains(@resource-id, 'switch_button')]")) >= 1
        # assert "someting" in driver.find*

    def test_parametric_management(self):
        TestCase("../Data/testcasedata.yaml").run(self.driver)
        assert "开启" in self.driver

    def test_demo2(self):
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[3]"
        ).click()
        self.driver.find_element_by_id("switch_button").click()
        text = self.driver.find_element_by_id("switch_button")
        assert "开启" in text.get_attribute("text")

    def test_po_demo(self):
        voice_page = VoicePage(self.driver)
        voice_page.xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[3]"
        )
        voice_page.search("switch_button")
        assert "开启" in voice_page.get_text()

    def test_swipe(self):
        self.driver.swipe(30, 1475, 30, 671, 700)
        sleep(1)

    def teardown(self):
        # os.system("adb reboot")
        self.driver.quit()


class TestCase:
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
