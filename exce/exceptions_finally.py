# -*- coding: utf-8 -*-
"""
    :author: allen lv
"""
import sys
import time

f = None
try:
    f = open('poem.txt')
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        sys.stdout.flush()
        # print('press ctrl+c now')
        # time.sleep(2)
except IOError:
    print('Could not find file poem.text')
except KeyboardInterrupt:
    print('!! you cancel the reading from the file')
finally:
    if f:
        f.close()
    print('file is closed')
