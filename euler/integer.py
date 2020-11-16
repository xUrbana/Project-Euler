import math
import itertools

def factorize(n):
    """Yields the factor pairs (a, b) of n such that a * b = n."""
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            yield (i, n // i)

def is_prime(n):
    """Return true if n is prime, otherwise false."""
    n = int(n)

    if n == 1: return False
    if n == 2: return True
    if n % 2 == 0: return False

    return not any(n % i == 0 for i in range(3, math.ceil(math.sqrt(n)) + 1, 2))

def iterprimes():
    """Yields primes one by one."""
    for i in itertools.count(start=2):
        if is_prime(i):
            yield i

def n_primes(n):
    """The first n primes."""
    return itertools.islice(iterprimes(), n)

def prime_factorize(n):
    """Yields the prime factors of n."""
    if n < 0:
        n = -n

    if n == 1:
        raise ValueError('1 has no prime factors')
    
    d = 2
    while n > 1:
        while n % d == 0:
            yield d
            n /= d
        d += 1

def nth_prime(n):
    """The nth prime number."""
    return next(itertools.islice(iterprimes(), n-1, n))