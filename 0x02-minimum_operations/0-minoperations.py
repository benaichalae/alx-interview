#!/usr/bin/python3


def minOperations(n):
    """
    This function calculates the minimum number of operations (Copy All, Paste)
    needed to achieve a desired number 'n' of characters (all 'H').

    Args:
        n: The target number of characters.

    Returns:
        The minimum number of operations needed, or 0 if impossible.
    """

    # Create a table to store minimum operations
    # for reaching different character counts
    dp = [float('inf')] * (n + 1)

    # Base case: 0 characters requires no operations
    dp[0] = 0

    # Iterate through possible character counts (1 to n)
    for i in range(1, n + 1):
        # Check if copying and pasting a smaller count is beneficial
        for j in range(1, i):
            # Ensure j divides i perfectly (pasting a non-multiple won't work)
            if i % j == 0:
                # Update dp[i] if the current option is less
                dp[i] = min(dp[i], dp[j] + 2)

    # Return the minimum operations for reaching n characters
    return dp[n] if dp[n] != float('inf') else 0
