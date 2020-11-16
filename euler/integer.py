from math import sqrt

def factorize(n):
    """Yields the factor pairs (a, b) of n such that a * b = n."""
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            yield (i, n // i)