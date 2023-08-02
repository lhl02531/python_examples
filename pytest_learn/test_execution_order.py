# -*- coding: utf-8 -*-
"""
    :author: allen lv
    方法的执行顺序
"""
import pytest


@pytest.mark.first
def test_02():
    print(2)


@pytest.mark.run(order=1)
def test_01():
    print(1)


class TestCls:

    def test_04(self):
        print(4)

    def test_03(self):
        print(3)


if __name__ == '__main__':
    pytest.main(['test_execution_order.py'])
