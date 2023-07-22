# -*- coding: utf-8 -*-
"""
    :author: allen lv
    进程之间通信
"""
from multiprocessing import Process, Queue
import os, time, random

def write(q):
    print('process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    print('process to read: %s' % os.getpid())
    # 这是个死循环，必须要有终止条件
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__ == '__main__':
    # 父进程创建 queue, 并传给各个子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程 pr和 pw
    pw.start()
    pr.start()

    # 等待 pw 结束
    pw.join()

    # pr 进程里是死循环，只能强行终止
    pr.terminate()