#!/usr/bin/python3

def is_winner(rounds, numbers):
    if rounds <= 0 or numbers is None:
        return None
    if rounds != len(numbers):
        return None

    ben_score = 0
    maria_score = 0
    primes = [1] * (max(numbers) + 1)
    primes[0], primes[1] = 0, 0

    for i in range(2, len(primes)):
        mark_non_primes(primes, i)

    for n in numbers:
        if sum(primes[:n + 1]) % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1

    if ben_score > maria_score:
        return "Ben"
    if maria_score > ben_score:
        return "Maria"
    return None

def mark_non_primes(array, number):
    for i in range(2, len(array)):
        try:
            array[i * number] = 0
        except (ValueError, IndexError):
            break

