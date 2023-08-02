# -*- coding: utf-8 -*-
"""
    :author: allen lv
    pytest&&allure
"""
import pytest


def add(a,b):
    return a+b

def test_case1():
    assert 1 == add(1,1)


def test_case2():
    assert 2 == add(1,1)


def test_case3():
    assert 3 == add(1,2)


def test_case4():
    assert 4 == add(3, 2)


def test_case5():
    assert 5 == add(3, 2)


def test_case6():
    assert 5 == add(4, 3)


if __name__ == '__main__':
    pytest.main(['test_use_allure.py'])