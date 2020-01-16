import math
import itertools

def is_prime(n):
    n = int(n)

    if n == 1: return False
    if n == 2: return True
    if n % 2 == 0: return False

    for i in range(3, math.ceil(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True

def iterprimes():
    for i in itertools.count(start=2):
        if is_prime(i):
            yield i

def nprimes(n):
    return itertools.islice(iterprimes(), n)

def prime_factorize(n):
    if n == 1:
        raise ValueError('1 has no prime factors')

    if n < 0:
        n = -n
    
    d = 2

    while n > 1:
        while n % d == 0:
            yield d
            n /= d
        d += 1

def nth_prime(n):
    return next(itertools.islice(iterprimes(), n-1, n))