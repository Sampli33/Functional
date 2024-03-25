import functools
import time


def limiter(running_time=None, calls = None):

    def decorator(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            wrapper.count += 1
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            if end_time > start_time + running_time:
                raise TimeoutError
            wrapper.count += 1
            if wrapper.count / 2 > calls:
                raise Exception('Превышено количество вызовов функции')
            return result

        wrapper.count = 0
        return wrapper
    return decorator


@limiter(2, 1)
def long_running_function():
    time.sleep(1)
    return "Function finished"



print(long_running_function())
print(long_running_function())
