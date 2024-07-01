#!/usr/bin/python3
"""
Function to determine the fewest number
of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """Returns the minimum number of coins needed to meet the total amount,
    or -1 if it's not possible with the given coins."""

    # Sort coins in descending order for optimal greedy approach
    coins.sort(reverse=True)

    # Initialize variables
    num_coins = 0
    remaining_amount = total

    # Iterate through each coin denomination
    for coin in coins:
        if remaining_amount <= 0:
            break

        # Calculate how many coins of this denomination can be used
        num_coins += remaining_amount // coin
        remaining_amount %= coin

    # If remaining_amount is 0, it means the total amount is achievable
    if remaining_amount == 0:
        return num_coins
    else:
        return -1
