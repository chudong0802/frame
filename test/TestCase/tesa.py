# coding=utf-8

"""
author: MiaZhang
Created on 2020/7/22 10:45
"""
import allure


@allure.title('测试用例集')
@allure.feature("中文录入，测试allure使用-feature")
class TestAllure:

    @allure.title('这是用例名称，代替用例的函数名')
    @allure.description('这是用例描述')
    @allure.story("--测试stroy")
    def test_01(self):
        with allure.step("步骤1"):
            a = 1
            assert a == 1
        with allure.step('步骤2'):
            b = 1
            assert a == b
        with allure.step('步骤3'):
            c = 1
            assert c == b
        with allure.step('步骤4'):
            d = 1
            assert d == c
        with allure.step('步骤5'):
            e = 1
            assert e == d

    @allure.title('这是用例名称')
    @allure.story('--测试stroy')
    def test_02(self):
        assert 1

    @allure.title('代替用例的函数名')
    @allure.story('--测试stroy')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_04(self):
        print("11")
        print(1)
        assert 1

    @allure.feature('feature1')
    @allure.title('这是用例名称1')
    @allure.story('story1')
    def test_sum_01(self):
        a = 1 + 1
        assert a == 2

    @allure.feature('feature2')
    @allure.title('这是用例名称2')
    @allure.story('story2')
    def test_sum_02(self):
        b = 1 + 2
        assert b == 1

    @allure.feature('feature2')
    @allure.title('这是用例名称3')
    @allure.story('story2')
    def test_sum_03(self):
        b = 1 + 2
        assert b == 1

    @allure.feature('feature2')
    @allure.title('这是用例名称4')
    @allure.story('story2')
    def test_sum_04(self):
        b = 1 + 2
        assert b == 1