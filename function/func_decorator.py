# -*- coding: utf-8 -*-
"""
    :author: allen lv
    decorator, 装饰器
"""
import functools, time
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now():
    print('2023-7-17')


now()   # 相当于 log(now)


def log1(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s()' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper

    return decorator

@log1('执行')
def now1():
    print('2023-7-17')
# 首先执行log('execute')，返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数。
now1()


def log2(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('%s' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log2
def now2():
    print('23-7-17')

now2()
print(now2.__name__)


def log3(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s()' %(text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log3('执行')     # log3('')
def now3():
    print('23-7-17')

now3()
print(now3.__name__)


# 测试
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start = time.time()
        res = fn(*args, **kw)
        end = time.time()
        print('%s executed in %s ms' % (fn.__name__,  end - start ))
        return res

    return wrapper
# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')


def call(text='call'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('begin %s' % text)
            res = func(*args, **kw)
            print('end %s' % text)
            return res
        return wrapper
    return decorator
@call()
def func1():
    print('func1')
    return 'func1'

@call('执行')
def func2():
    print('func2')
    return 'func2'

f1 = func1()
f2 = func2()
print('%s %s' %(f1, f2))