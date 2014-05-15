"""Created by madhusudan email: msbanik@gmail.com on 2014-05-14 22:12:59.
"""

from functools import wraps


class A:
    def decorator1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('decorator1')
            return func(*args, **kwargs)

        return wrapper

    def decorator2(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('decorator2')
            return func(*args, **kwargs)

        return wrapper


a = A()


@a.decorator1
def spam():
    print('spam')


@a.decorator2
def gork():
    print('gork')


spam()
gork()