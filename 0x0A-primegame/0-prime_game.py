#!/usr/bin/python3
"""Module for Prime Game"""


def isWinner(x, nums):
    # Check for invalid input conditions
    if x <= 0 or not nums or x != len(nums):
        return None

    # Helper function to generate prime numbers
    # up to n using Sieve of Eratosthenes
    def sieve_of_eratosthenes(n):
        # Initialize a list to mark prime numbers
        is_prime = [True] * (n + 1)
        p = 2
        # Mark non-primes starting from 2 up to sqrt(n)
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        # 0 and 1 are not prime numbers
        is_prime[0] = is_prime[1] = False
        return is_prime

    # Find the maximum number in nums
    # to determine the range for prime calculation
    max_num = max(nums)
    # Generate a list of prime numbers using the helper function
    primes = sieve_of_eratosthenes(max_num)

    # Initialize counters for Ben and Maria's wins
    ben = 0
    maria = 0

    # Iterate over each round in nums
    for n in nums:
        # Calculate the sum of prime numbers up to n
        if sum(primes[:n + 1]) % 2 == 0:
            # If the sum is even, Ben wins the round
            ben += 1
        else:
            # Otherwise, Maria wins the round
            maria += 1

    # Determine the winner based on who won more rounds
    if ben > maria:
        return "Ben"
    elif maria > ben:
        return "Maria"
    else:
        # If Ben and Maria won the same number of rounds, return None
        return None
