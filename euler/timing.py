import time
import functools

def timed(func):
    """Decorator that prints the elapsed time the wrapped function takes."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        s = time.time()
        ret = func(*args, **kwargs)
        e = time.time() - s
        print(f'{func.__name__} took {e} seconds to complete!')
        return ret
    return wrapper
