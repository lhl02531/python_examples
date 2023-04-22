# -*- coding: utf-8 -*-
"""
    :author: allen lv
    :source from https://www.liaoxuefeng.com/wiki/1016959663602400/1017455068170048
"""
import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('hello world')
    elif len(args) == 2:
        print('hello, %s' % args[1])
    else:
        print('too many arguments')

if __name__ == '__main__':
    test()