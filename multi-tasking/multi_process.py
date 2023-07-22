# -*- coding: utf-8 -*-
"""
    :author: allen lv
    进程
"""
from multiprocessing import Process
import os


# 子进程要执行的代码
def run_proc(name):
    print('run child process %s (%s)...' % (name, os.getpid()))

if __name__ == '__main__':
    print('parent process id: %s.' % os.getpid())
    # args是元组，当元组一个元素是，记得加逗号,
    p = Process(target=run_proc, args=('test', ))
    print('child process will start.')
    p.start()
    # 等子进程结束再继续往下执行
    p.join()
    print('child process will end')