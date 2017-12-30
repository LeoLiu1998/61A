## Lab 13: Coroutines ##

# Q3

def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    while n != 1:
        yield int(n)
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1
    yield 1
