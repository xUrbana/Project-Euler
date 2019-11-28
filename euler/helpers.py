import math
import itertools

def is_prime(n):

    if isinstance(n, str):
        n = int(n)

    if n == 1: return False
    if n == 2: return True
    if n % 2 == 0: return False

    for i in range(3, math.ceil(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True

def iterprimes():
    for i in itertools.count(2):
        if is_prime(i):
            yield i

def rotations(s: str):
    # We can find all rotations by appending the string to itself
    ss = s + s
    for i in range(len(s)):
        yield ss[i:i+len(s)]