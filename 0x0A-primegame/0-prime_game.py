#!/usr/bin/python3
"""Code to determine to winner of the prime game"""


def is_prime(n):
    """
    Checks if a number n is a prime number.

    Args:
    n (int): The number to check.

    Returns:
    bool: True if n is prime, False otherwise.
    """
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return False
    return True


def calculate_primes(n, primes):
    """
    Calculate all prime numbers up to n and store them in the 'primes' list.

    Args:
    n (int): The upper limit for prime number calculation.
    primes (list): A list to store prime numbers.
    """
    top_prime = primes[-1]
    if n > top_prime:
        for i in range(top_prime + 1, n + 1):
            if is_prime(i):
                primes.append(i)
            else:
                primes.append(0)


def isWinner(x, nums):
    """
    Determine the winner of a game played for 'x' rounds.

    Args:
    x (int): The number of rounds to be played.
    nums (list): An array of integers 'n', 
    where each 'n' is the upper limit for prime number calculation.

    Returns:
    str: The name of the player that won the most rounds ('Maria' or 'Ben').
         If the winner cannot be determined, returns None.
    """
    players_wins = {"Maria": 0, "Ben": 0}

    primes = [0, 0, 2]

    calculate_primes(max(nums), primes)

    for round in range(x):
        sum_options = sum((i != 0 and i <= nums[round])
                          for i in primes[:nums[round] + 1])

        if (sum_options % 2):
            winner = "Maria"
        else:
            winner = "Ben"

        if winner:
            players_wins[winner] += 1

    if players_wins["Maria"] > players_wins["Ben"]:
        return "Maria"
    elif players_wins["Ben"] > players_wins["Maria"]:
        return "Ben"

    return None
