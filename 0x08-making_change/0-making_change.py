#!/usr/bin/python3

def makeChange(coins, total):
  """
  This function determines the fewest number of coins needed to meet a given amount.
  """

  # Handle base cases
  if total == 0:
    return 0
  elif total < 0:
    return -1

  # Initialize a table to store the minimum number of coins needed for each amount up to the total
  dp = [float('inf')] * (total + 1)

  # Initialize the minimum number of coins needed for 0 amount as 0
  dp[0] = 0

  # Iterate through each coin denomination
  for coin in coins:
    # For each amount from 0 to the total, update the minimum number of coins if possible
    for amount in range(coin, total + 1):
      dp[amount] = min(dp[amount], dp[amount - coin] + 1)

  # Check if the total amount can be made with the available coins
  return dp[total] if dp[total] != float('inf') else -1
