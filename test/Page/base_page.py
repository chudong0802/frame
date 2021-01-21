#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @Site: 
# @File: base_page.py
# @Author: JasonWu
# @E-mail: 15000257149@163.com
# @Time: 5月 07, 2020
# ---
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from Utils.log_config import LogConfig

from appium import webdriver
from appium.webdriver.webdriver import WebDriver
import time
import os


class BasePage:
    _black_list = [
        (By.ID, "image_cancel"),
        (By.ID, "tips"),
        (By.ID, "set_vehicle_dialog_dismiss_bt"),
        (By.ID, "tv_content")
    ]
    __logger = LogConfig().Logger

    def __init__(self, driver: WebDriver):
        self.driver = driver


    @property
    def logger(self):
        return self.__logger

    def find_element(self, locator):
        try:
            self.logger.info('开始定位元素：' + locator[0] + '：' + locator[1])
            return self.driver.find_element(*locator)
        except:
            self.logger.error('元素定位失败：' + locator[0] + '：' + locator[1])
            self.handle_exception()
            # self.find_element(locator)
            self.logger.info('第二次开始定位元素：' + locator[0] + '：' + locator[1])
            return self.driver.find_element(*locator)

    def find_element_and_click(self, locator):
        try:
            self.find_element(locator).click()
            self.logger.info('元素点击成功：' + locator[0] + '：' + locator[1])
        except:
            self.logger.error('元素点击失败：' + locator[0] + '：' + locator[1])
            self.handle_exception()
            self.logger.info('第二次定位元素并点击：' + locator[0] + '：' + locator[1])
            self.find_element(locator).click()

    def handle_exception(self):
        ##异常行为处理，各类弹框
        # print(":exception")

        # kill navigation package

        os.system('adb shell \"pidof com.hryt.navigation\" > 1.txt')
        os.system('adb root')
        os.system('adb remount')
        with open("1.txt", 'r', encoding='utf-8') as f:
            lines = f.readlines()
            print(lines[0])
            os.system('adb shell kill ' + lines[0])

        self.driver.implicitly_wait(1)
        for locator in self._black_list:
            try:
                self.logger.info('弹出框处理中：' + locator[0] + '：' + locator[1])
                elements = self.driver.find_element(*locator)
                self.find_element_and_click(*locator)
                if len(elements) >= 1:
                    # 不是所有的弹框处理都是要点击弹框，可根据业务需要自行封装
                    elements[0].click()
                else:
                    print("%s not found" % str(locator))
            except:
                self.logger.error('弹出框处理失败：' + locator[0] + '：' + locator[1])

            # 私用page source会更快的定位

            # page_source=self.driver.page_source
            # if "image_cancel" in page_source:
            #     self.driver.find_element(*locator).click()
            # elif "tips" in page_source:
            #     pass

        self.driver.implicitly_wait(10)

    def element_clear(self, locator):
        try:
            self.find_element(locator).clear()
            self.logger.info('输入框字符清空成功：' + locator[0] + '：' + locator[1])
        except:
            self.logger.error('输入框字符清空失败：' + locator[0] + '：' + locator[1])
            self.handle_exception()

    def element_send_keys(self, locator, value):
        try:
            self.find_element(locator).send_keys(value)
            self.logger.info('输入框字符键入成功：' + locator[0] + '：' + locator[1])
        except:
            self.logger.error('输入框字符键入失败：' + locator[0] + '：' + locator[1])
            self.handle_exception()

    def element_double_tap(self, locator):
        try:
            actions = TouchAction(self.driver)
            actions.double_tap(self.find_element(locator))
            actions.perform()
            self.logger.info('元素双击成功：' + locator[0] + '：' + locator[1])
        except:
            self.logger.error('元素双击失败：' + locator[0] + '：' + locator[1])
            self.handle_exception()



# if __name__ == "__main__":
#     os.system('adb root | adb remount | adb shell \"pidof com.hryt.navigation\" > 1.txt')
#     with open("1.txt", 'r', encoding='utf-8') as f:
#         lines = f.readlines()
#         print(lines[0])
#         os.system('adb shell kill ' + lines[0])
#     driver: WebDriver = None
#     caps = {}
#     caps["autoGrantPermissions"] = True
#     caps["platformName"] = "android"
#     caps["deviceName"] = "whatever"
#     caps["appActivity"] = ".MainActivity"
#     caps["appPackage"] = "com.hryt.navigation"
#     caps["unicodeKeyboard"] = True
#
#     driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
#     driver.implicitly_wait(10)
#
#     # 留给开启时的定制化处理，比如：升级框，电量不足，信息通知等等
#     # try:
#     #     WebDriverWait(self.driver, 20).until(loaded)  #loaded封装到Utils.wait_tool中
#     # except:
#     #     print("sometings")
#     time.sleep(180)
#     b = BasePage(driver)
#     b.handle_exception()
#
#     driver.quit()
