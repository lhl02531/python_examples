# -*- coding: utf-8 -*-
"""
    :author: allen lv
    使用断言
"""
import pytest


def add(a, b):
    return a + b


def test_equal():
    assert 5 == add(1, 5)


if __name__ == '__main__':
    pytest.main(['test_use_assert.py'])
