from euler.fibonacci import iterfibs

def euler25():
    '''https://projecteuler.net/problem=25'''
    for i,fib in enumerate(iterfibs()):
        if len(str(fib)) >= 1000:
            return i + 1
