# -*- coding: utf-8 -*-
"""
    :author: allen lv
"""


def _pri_fun_1(name):
    print('hello, %s' % name)


def _pri_fun_2(name):
    print('Hi, %s' % name)


def greeting(name):
    if len(name) > 3:
        _pri_fun_1(name)
    else:
        _pri_fun_2(name)
