#!/usr/bin/python3
"""Minimum Operations"""

def minOperations(n):
    """
    This function calculates the minimum number of operations (Copy All, Paste)
    needed to achieve a desired number 'n' of characters (all 'H').

    Args:
        n: The target number of characters.

    Returns:
        The minimum number of operations needed, or 0 if impossible.
    """

    if not isinstance(n, int):
        return 0
    ops_count = 0
    clipboard = 0
    while n > 1:
        if n % 2 == 0:
            n //= 2
            ops_count += 1
        else:
            clipboard = n
            n -= clipboard
            ops_count += 2
    return ops_count
