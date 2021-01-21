# coding=utf-8

"""
author: MiaZhang
Created on 2020/9/8 13:50
"""
import allure
from selenium.webdriver.common.by import By

from Page.base_page import BasePage


class BodyControlMainPage(BasePage):

    _switch_in_car_locator = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.Button")
    _main_driver_seat_setting = (By.ID, "com.hryt.bodycontrol:id/btn_front_left")
    _copilot_seat_setting = (By.ID, "com.hryt.bodycontrol:id/btn_fr")
    _switch_outside_the_car = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.Button")

    def in_car_page(self):
        allure.epic('Body Control')
        allure.feature('in car page')
        self.find_element(self._switch_in_car_locator).click()
        self.logger.info('跳转到车内页面成功')
        self.find_element(self._main_driver_seat_setting).click()
        self.logger.info('进入主驾驶座椅设置页面成功')
        self.find_element(self._copilot_seat_setting).click()
        self.logger.info('进入副驾驶座椅设置成功')
        return self

    def outside_the_car_page(self):
        allure.epic('Body Control')
        allure.feature('outside the car page')
        self.find_element(self._switch_outside_the_car).click()
        self.logger.info('跳转到车外页面成功')
        return self
