import functools
from datetime import datetime


def logger(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except Exception as error:
                with open(f'{func.__name__}.txt', 'w') as f:
                    print(datetime.now(), f'{type(error).__name__}: {str(error)}', file=f)
                raise

    return wrapper


@logger
def printer():
    print(10 / 0)


printer()
