# -*- coding: utf-8 -*-
"""
    :author: allen lv
    lock
"""
import time, threading
# 假设这是存款
balance = 0
# 锁初始化
lock = threading.Lock()
def change_it(n):
    # 先存后去，结果应该为0
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(2000000):
        # 先获取锁
        lock.acquire()
        try:
            # 操作
            change_it(n)
        finally:
            # 最后记得释放锁
            lock.release()



t1 = threading.Thread(target=run_thread, args=(5, ))
t2 = threading.Thread(target=run_thread, args=(8, ))
t1.start()
t2.start()

t1.join()
t2.join()
print(balance)
