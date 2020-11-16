from euler.fibonacci import iterfibs

def euler25():
    """What is the index of the first term in the Fibonacci sequence to contain 1000 digits?"""
    for i,fib in enumerate(iterfibs()):
        if len(str(fib)) >= 1000:
            return i + 1
