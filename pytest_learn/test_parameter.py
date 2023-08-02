# -*- coding: utf-8 -*-
"""
    :author: allen lv
    pytest 参数化
"""
import pytest


def add(a, b):
    return a + b


# 1
t2 = [(3, 1), (1, 4), (3, 2), (2, 2)]


# 2
@pytest.mark.skip
@pytest.mark.parametrize(['x', 'y'], [(1, 2), (1, 4), (0, 5)])
def test_add_1(x, y):
    assert 5 == add(x, y)


# 3
t3 = [{'a':1,'b':2, 'c':2},{'a':2,'b':3, 'c':3},{'a':3,'b':4, 'c':4}]

@pytest.mark.skip
@pytest.mark.parametrize(['x', 'y'], t2)
def test_add_2(x, y):
    assert 5 == add(x, y)

@pytest.mark.parametrize("a, b , c", t3)
def test_add_2(a, b, c):
    print(a, b, c)
    assert 5 == (a + b + c)


if __name__ == '__main__':
    pytest.main(['test_parameter.py'])
