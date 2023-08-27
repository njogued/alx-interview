#!/usr/bin/python3
"""fewest number of coins needed for a certain amount
"""


def makeChange(coins, total):
    """Calculate the coins needed to make total"""
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    change = 0
    for coin in coins:
        if total <= 0:
            break
        temp = total // coin
        change += temp
        total -= (temp * coin)
    if total != 0:
        return -1
    return change
