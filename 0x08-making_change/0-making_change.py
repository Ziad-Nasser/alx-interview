#!/usr/bin/python3
"""
Implement Making Change function.
"""


def makeChange(coins, total):
    """
    Make Change function.

    Args:
        coins (list): A list of the values of the coins.
        total (int): The total value of coins needed.

    Returns:
        int: The fewest number of coins needed to make up the given total value,
             or -1 if it's not possible.
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0

    change = 0
    coins = sorted(coins, reverse=True)

    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if total == 0:
            return change

    return -1
