#!/usr/bin/python3

""" Contains makeChange function """

def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet the total amount.
    """
    if total <= 0:
        return 0

    # Sort the coins in descending order to try using the largest coins first
    coins = sorted(coins, reverse=True)
    change = 0

    for coin in coins:
        # Use as many coins of the current denomination as possible
        if total >= coin:
            change += total // coin
            total %= coin

        # If the total is reduced to 0, return the number of coins used
        if total == 0:
            return change

    # If total is not 0 after iterating through all coins, return -1
    return -1
