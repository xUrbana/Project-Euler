from euler.primes import iterprimes
from euler.string import pandigital
import itertools

def euler41():
    '''
    We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

    What is the largest n-digit pandigital prime that exists?
    '''

    possible_primes = itertools.takewhile(lambda p: p <= 987654321, iterprimes())
    return max(possible_primes)

print(euler41())




