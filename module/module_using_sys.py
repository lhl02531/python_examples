# -*- coding: utf-8 -*-
"""
    :author: allen lv
"""
import sys
from module_using_name import fun_dect

print('The command line arguments are:')
for i in sys.argv:
    print(i)

print('\n\n the pythonpath is', sys.path, '\n')
print('\n')
fun_dect()
