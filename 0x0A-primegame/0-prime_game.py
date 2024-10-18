#!/usr/bin/python3

"""
Prime Game
"""
def find_multiples(num, targets):
    """
    Remove multiples of the given number from the list.
    """
    or i in targets[:]:
        if i % num == 0:
            targets.remove(i)
    return targets
def is_prime(i):
    if i <= 1:
        return False
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            return False
    return True
def find_primes(n):
    prime_count = 0
    targets = list(n)

    for i in range(2, max(targets) + 1):
        if is_prime(i):
            prime_count += 1
            if i in targets:
                targets.remove(i)
            targets = find_multiples(i, targets)

    return prime_count

def isWinner(x, nums):
    players = {'Maria': 0, 'Ben': 0}

    for game_round in range(x):
        n = nums[game_round]
        numbers = set(range(1, n + 1))
        prime_count = find_primes(numbers)

        # Determine who wins this round based on the number of primes found
        if prime_count % 2 == 0:
            players['Ben'] += 1
        else:
            players['Maria'] += 1

    if players['Maria'] > players['Ben']:
        return 'Maria'
    elif players['Ben'] > players['Maria']:
        return 'Ben'
    else:
        return None
