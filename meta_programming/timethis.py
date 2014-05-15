"""Created by madhusudan email: msbanik@gmail.com on 5/14/14.
put a wrapper layer around a function
"""

import time
from functools import wraps


def timethis(func):
    """calculate the execution time of a function"""

    @wraps(func)  # preserve function metadata
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return wrapper


@timethis
def countdown(n):
    """count down"""
    while n > 0:
        n -= 1


countdown(1000000)
print countdown.__doc__
