import functools


def print_result(func):

    @functools.wraps(func)
    def wrapper(arg):
        print(func(arg))

    return wrapper


@print_result
def squaring(number):
    return number ** 2


squaring(6)
