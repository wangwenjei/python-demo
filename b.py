"""
def outter(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        stop = time.time()
        print("timeout:", stop - start)
        return res

    return wrapper
"""

import time


def outter(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        stop = time.time()

        print("timeout:", stop - start)
        return res

    return wrapper


@outter
def index():
    time.sleep(1)
    return '被装饰对象'


print(index())