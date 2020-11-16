from euler.integer import iterprimes, is_prime
from euler.string import rotations

def euler35():
    """The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
    There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
    How many circular primes are there below one million?
    """
    circular_primes = 0

    for prime in iterprimes():
        if prime >= 1000000:
            break

        if all(is_prime(rp) for rp in rotations(str(prime))):
            circular_primes += 1
    
    return circular_primes
    


    