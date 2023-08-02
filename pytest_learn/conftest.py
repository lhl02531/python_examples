# -*- coding: utf-8 -*-
"""
    :author: allen lv
"""
import pytest


@pytest.fixture()
def first_fixture():
    print('first fixture')
    return '1'


@pytest.fixture()
def second_fixture():
    print('second fixture')
    return '2'
