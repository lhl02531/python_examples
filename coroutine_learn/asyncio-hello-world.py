# -*- coding: utf-8 -*-
"""
    :author: allen lv
    asyncio hello world
"""
import asyncio


async def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1):
    # r = yield from asyncio.sleep(1)
    await asyncio.sleep(1)
    print("Hello again!")

# @asyncio.coroutine
# def hello():
#     print("Hello world!")
#     # 异步调用asyncio.sleep(1):
#     r = yield from asyncio.sleep(1)
#     print("Hello again!")


# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()
