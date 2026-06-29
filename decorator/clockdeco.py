import time
import functools


def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_lst = [i for i in args]
        # print(f'[{elapsed:0.8f}s] {name}({arg_lst}) -> {result!r}')

        return result
    
    return clocked


@functools.cache
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)


t0 = time.perf_counter()
print(fibonacci(35))

print(time.perf_counter() - t0)
