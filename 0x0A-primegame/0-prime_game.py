#!/usr/bin/python3
"""Function to determine the winner of the prime game"""


def isWinner(x, nums):
    def isPrime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def canWin(n):
        dp = [False] * (n + 1)
        dp[0] = False  # Maria can't win with 0 numbers left
        dp[1] = False  # Maria can't win with 1 number left

        for i in range(2, n + 1):
            if isPrime(i):
                dp[i] = True
                continue
            for j in range(2, i):
                if i % j == 0 and not dp[i - j]:
                    dp[i] = True
                    break

        return dp[n]

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if canWin(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Ben"
    elif ben_wins > maria_wins:
        return "Maria"
    else:
        return None
