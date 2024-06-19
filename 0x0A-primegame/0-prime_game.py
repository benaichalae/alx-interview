#!/usr/bin/python3
"""Module for Prime Game"""


def is_winner(x, nums):
    """
    Determines the winner of a series of prime number games.

    Args:
        x (int): The number of rounds to be played.
        nums (list of int): A list of integers,
        each representing the range of numbers to be used in a round.

    Returns:
        str: The name of the player who won the most rounds ("Ben" or "Maria").
        None: If no clear winner can be determined.
    """
    if x <= 0 or not nums or x != len(nums):
        return None

    ben_wins, maria_wins = 0, 0
    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)

    for n in nums:
        if sum(primes[:n + 1]) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if ben_wins > maria_wins:
        return "Ben"
    elif maria_wins > ben_wins:
        return "Maria"
    else:
        return None


def sieve_of_eratosthenes(limit):
    """
    Generates a list of prime indicators up to
    a specified limit using the Sieve of Eratosthenes algorithm.

    Args:
        limit (int): The upper limit for generating prime indicators.

    Returns:
        list of int: A list where indices represent numbers
        and values indicate primality (1 for prime, 0 for non-prime).
    """
    primes = [1] * (limit + 1)
    primes[0], primes[1] = 0, 0

    for i in range(2, int(limit ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = 0

    return primes
