import itertools

def euler5():
    """2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    """
    for n in itertools.count(start=20, step=20):
        if all(n % i == 0 for i in range(11, 20)):
            return n
