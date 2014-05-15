"""Created by madhusudan email: msbanik@gmail.com on 2014-05-14 21:31:25.
"""

from functools import wraps
import logging


def logged(level, name=None, message=None):
    """
    @level: logging level
    @name: logger name
    @message: log message
    """

    def decorate(func):
        logname = name or func.__module__
        log = logging.getLogger(logname)
        logmsg = message or func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        return wrapper

    return decorate


@logged(logging.DEBUG, 'example')
def add(x, y):
    return x + y


@logged(logging.CRITICAL, 'spam spam')
def spam():
    print ('Spam!')


# add = logged(logging.CRITICAL, 'spam')(add)
add(2, 3)
spam()