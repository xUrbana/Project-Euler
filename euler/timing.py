import time
import functools

# Crude timing decorator for functions
def timed(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        s = time.time()
        ret = func(*args, **kwargs)
        e = time.time() - s
        print(f'{func.__name__} took {e} seconds to complete!')
        return ret
    return wrapper
