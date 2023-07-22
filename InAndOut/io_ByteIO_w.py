# -*- coding: utf-8 -*-
"""
    :author: allen lv
    ByteIO write
"""
from io import BytesIO
f = BytesIO()
f.write('朝辞白帝彩云间，'.encode('utf-8'))
print(f.getvalue())