#!/usr/bin/python3
"""
A a method that calculates the fewest
number of operations needed to result
in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Finds the minimum operation

    Args:
        n (int): The n
    """
    if n <= 1:
        return 0
    factor = 2
    operation = 0
    while n > 1:
        while n % factor == 0:
            operation += factor
            n = n // factor
        factor += 1
    return operation
