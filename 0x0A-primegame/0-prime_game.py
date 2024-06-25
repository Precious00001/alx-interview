#!/usr/bin/python3
"""Prime game module."""


def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds.

    Args:
        x (int): The number of rounds in the prime game session.
        nums (list): A list of integers representing numbers for each round.

    Returns:
        str or None: The name of the winner ('Maria' or 'Ben') or None if the
        number of wins for Maria and Ben are equal.

    """
    # Check if the number of rounds is valid or if nums list is empty
    if x < 1 or not nums:
        return None

    # Initialize variables to count Maria's and Ben's wins
    marias_wins, bens_wins = 0, 0

    # Generate primes with a limit of the maximum number in nums
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False

    # Sieve of Eratosthenes algorithm to mark non-primes
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False

    # Determine the winner for each round
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1

    # Compare the number of wins for Maria and Ben
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
