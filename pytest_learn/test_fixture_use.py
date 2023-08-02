# -*- coding: utf-8 -*-
"""
    :author: allen lv
    pytest fixture
"""
import pytest


@pytest.fixture()
def first_fixture():
    print('first fixture')
    return 'first'


@pytest.fixture()
def second_fixture(first_fixture):
    print('second')
    return 'second plus ' + first_fixture


@pytest.fixture()
def third_fixture():
    return 1, 2, 3


@pytest.fixture()
def fourth_fixture():
    return '4'


def test_case1(first_fixture):
    print('test case1')
    res = first_fixture
    print(res)


def test_case2(second_fixture):
    print('test case2')
    res = second_fixture
    print(res)


def test_case3(third_fixture):
    print('test case3')
    res = third_fixture
    print(res)
    assert (1, 2, 3) == third_fixture


def test_case4(third_fixture, fourth_fixture):
    print('test case4')
    assert (1, 2, 3) == third_fixture
    assert fourth_fixture == 4
