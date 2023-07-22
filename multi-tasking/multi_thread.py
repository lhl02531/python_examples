# -*- coding: utf-8 -*-
"""
    :author: allen lv
    线程使用
"""
import time, threading

# 新线程执行的代码
def loop():
    print('multi-tasking %s is running' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('multi-tasking %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('multi-tasking %s ended.' % threading.current_thread().name)


print('multi-tasking %s is running' % threading.current_thread().name)
# 启动线程就是把一个函数传入并创建 Thread 实例， 然后调用 start()开始执行
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('multi-tasking %s is ended' % threading.current_thread().name)