#!/usr/bin/python3

def makeChange(coins, total):
    # If total is 0 or less, no coins are needed
    if total <= 0:
        return 0

    # Initialize a list to store the minimum number
    dp = [total + 1] * (total + 1)

    # Zero coins are needed to make a total of 0
    dp[0] = 0

    # Build up the dp array by checking each amount from 1 to total
    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still total + 1
    return dp[total] if dp[total] != total + 1 else -1
