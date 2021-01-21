# coding=utf-8

"""
author: MiaZhang
Created on 2020/9/15 13:43
"""
import pytest

from Drivers.bodycontrol_driver import bodycontrolApp
from Drivers.energymonitor_driver import energymonitorApp


@pytest.fixture(scope="session")
def f_bodycontrol_App():
    yield bodycontrolApp.start()
    bodycontrolApp.quit()


@pytest.fixture(scope="session")
def f_energymonitor_App():
    yield energymonitorApp.start()
    energymonitorApp.quit()
