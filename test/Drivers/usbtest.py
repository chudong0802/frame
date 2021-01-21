from time import sleep
import pytest
from appium import webdriver
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from Page.usb_up import Usb_up
import os

def get_size():
    '''获取屏幕大小'''
    size_dict = driver.get_window_size()
    x = size_dict.get('width')
    y = size_dict.get('height')
    return x,y
def shrink():
    '''缩小'''
    x,y = get_size()
    print(x,y)
    action1 = TouchAction(driver)
    action2 = TouchAction(driver)
    add_action = MultiAction(driver)
    #指定操作
    action1.press(x=x * 0.4, y=y * 0.4).wait(1000).move_to(x=x * 0.2, y=y * 0.2).wait(1000).release()
    action2.press(x=x * 0.6, y=y * 0.6).wait(1000).move_to(x=x * 0.8, y=y * 0.8).wait(1000).release()
    add_action.add(action1,action2)
    #执行操作
    add_action.perform()


def usp_up():
    cap = {
        "autoGrantPermissions": True,
        "platformName": "android",
        "deviceName": "whatever",
        "appActivity": ".MainActivity",
        "appPackage": "com.example.hyan6.pma_upgrade_app",
        "unicodeKeyboard": True
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', cap)
    sleep(3)
    # size_dict = driver.get_window_size()
    # x = size_dict.get('width')
    # y = size_dict.get('height')
    # x, y = get_size()
    # print(x, y)
    action1 = TouchAction(driver)
    action2 = TouchAction(driver)
    add_action = MultiAction(driver)
    # 指定操作
    action1.press(x=20, y=1883).wait(1000).move_to(x=20, y=1000).wait(1000).release()
    action2.press(x=60, y=1883).wait(1000).move_to(x=60, y=1000).wait(1000).release()
    add_action.add(action1, action2)
    # 执行操作
    add_action.perform()
    driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.Button[1]").click()


if __name__ == '__main__':
    usp_up()

