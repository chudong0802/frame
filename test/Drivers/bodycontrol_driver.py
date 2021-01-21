# coding=utf-8

"""
author: MiaZhang
Created on 2020/9/8 13:48
"""
import os

from appium import webdriver
from appium.webdriver.webdriver import WebDriver

from Page.BodyControlMainPage import BodyControlMainPage


class bodycontrolApp:
    driver: WebDriver = None

    @classmethod
    def start(cls):
        # os.system('adb shell \"pidof com.hryt.navigation\" > 1.txt')
        # os.system('adb root')
        # os.system('adb remount')
        # with open("1.txt", 'r', encoding='utf-8') as f:
        #     lines = f.readlines()
        #     print(lines[0])
        #     os.system('adb shell kill ' + lines[0])
        caps = {}
        caps["autoGrantPermissions"] = True
        caps["platformName"] = "android"
        caps["deviceName"] = "whatever"
        caps["appActivity"] = ".ui.VehicleControlActivity"
        caps["appPackage"] = "com.hryt.bodycontrol"
        caps["unicodeKeyboard"] = True

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)

        # 留给开启时的定制化处理，比如：升级框，电量不足，信息通知等等
        # try:
        #     WebDriverWait(self.driver, 20).until(loaded)  #loaded封装到Utils.wait_tool中
        # except:
        #     print("sometings")

        return cls.driver

    @classmethod
    def quit(cls):
        cls.driver.quit()
