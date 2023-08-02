# -*- coding: utf-8 -*-
"""
    :author: allen lv
    前置
    后置
"""
import pytest


def setup_module():
    print('前置模块')


def teardown_module():
    print('后置模块')


def setup_function():
    print('前置函数')


def teardown_function():
    print('后置函数')


def test_01():
    print('func1')


def test_02():
    print('func2')

class TestCls:

    def setup_class(self):
        print('前置 class ')

    def teardown_class(self):
        print('后置 class ')

    def setup_method(self):
        print('前置 method ')

    def teardown_method(self):
        print('后置 method ')

    def test_03(self):
        print('func3')

    def test_04(self):
        print('func4')

if __name__ == '__main__':
    pytest.main(['test_before_after.py'])
