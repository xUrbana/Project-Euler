from euler.string import palindrome
import itertools

def euler4():
    '''
    A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit numbers.
    '''
    return max(n*m for n,m in itertools.combinations(range(100, 1000), 2) if palindrome(str(n*m)))