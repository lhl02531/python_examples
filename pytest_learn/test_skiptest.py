# -*- coding: utf-8 -*-
"""
    :author: allen lv
"""
import pytest


@pytest.mark.skip()
def test_case1():
    print('test case1')

a = 1
@pytest.mark.skipif(a>0, reason='if a > 0 pass')
def test_case2():
    print('test case22')


b = 1
@pytest.mark.skipif(b<0, reason='if a > 0 pass')
def test_case3():
    print('test case3')