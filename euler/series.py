from functools import reduce

def sum_of_naturals(n):
    """The sum of the first n natural numbers."""
    return (n * (n + 1)) // 2

def sum_of_squares(n):
    """The sum of the first n^2 natural numbers."""
    return (n * (n + 1) * (2 * n + 1)) // 6

def sum_of_cubes(n):
    """The sum of the first n^3 natural numbers."""
    return (n ** 2 * (n + 1) ** 2) // 4
