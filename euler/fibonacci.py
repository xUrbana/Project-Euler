
def iterfibs():
    """Yields the fibonacci numbers."""
    a = 1
    b = 1
    yield a
    yield b

    while True:
        c = a + b
        yield c
        a = b
        b = c