# coding=utf-8

"""
author: MiaZhang
Created on 2020/9/16 13:57
"""
import allure
import pytest


@allure.story('switch page')
@pytest.mark.run(order=1)
def test_1(f_energymonitor_App):
    f_energymonitor_App.switch_travel_statistics_page()
    assert 1


@allure.story('switch page')
@pytest.mark.run(order=2)
def test_2(f_energymonitor_App):
    f_energymonitor_App.switch_historical_power_consumption_page()
    assert 1


@allure.story('switch page')
@pytest.mark.run(order=3)
def test_3(f_energymonitor_App):
    f_energymonitor_App.switch_instant_power_consumption_page()
    assert 1


