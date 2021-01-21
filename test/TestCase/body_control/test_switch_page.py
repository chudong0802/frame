# coding=utf-8

"""
author: MiaZhang
Created on 2020/9/8 13:46
"""
import allure
import pytest


@allure.story('switch page')
@pytest.mark.run(order=1)
def test_switch_in_car_page(f_bodycontrol_App):
    f_bodycontrol_App.in_car_page()
    assert 1


@allure.story('switch page')
@pytest.mark.run(order=2)
def test_switch_outside_the_car_page(f_bodycontrol_App):
    f_bodycontrol_App.outside_the_car_page()
    assert 1

