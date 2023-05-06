# -*- coding: utf-8 -*-
"""
    :author: allen lv
"""
try:
    text = input('enter something -->')
except EOFError:
    print('EOFError')
except KeyboardInterrupt:
    print('you cancelled the operation.')
else:
    print('you enterd {}'.format(text))