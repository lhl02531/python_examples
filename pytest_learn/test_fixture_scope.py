# -*- coding: utf-8 -*-
"""
    :author: allen lv
"""
import pytest


@pytest.fixture(scope='session', autouse=True)
def session_fixture():
    print('session scope')


@pytest.fixture(scope='module', autouse=True)
def module_fixture():
    print('module scope')


@pytest.fixture(scope='class', autouse=True)
def class_fixture():
    print('class scope')


@pytest.fixture(scope='function', autouse=True)
def func_fixture():
    print('function scope')


# @pytest.fixture(scope='methods', autouse=True)
# def func_fixture():
#     print('methods scope')


def test_case1():
    print('case1')


def test_case2():
    print('case2')


class Test_cls():

    def test_case3(self):
        print('case 3')
