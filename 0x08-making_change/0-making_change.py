#!/usr/bin/python3

"""Implement Making Change function"""


def makeChange(coins, total):
    """Make Change function
    Args:
        coins: a list of the values of the coins
        total: the total value of coins needed
   RETURN: the fewest number of coins needed to make up the given value total
    
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    change = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if (total == 0):
            return change
    return -1