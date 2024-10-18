#!/usr/bin/python3

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return primes

def count_primes_up_to(primes, n):
    return sum(1 for i in range(1, n + 1) if primes[i])

def isWinner(x, nums):
    if not nums or x < 1:
        return None

    # Determine the maximum value of `n` to consider
    max_num = max(nums)
    
    # Use Sieve of Eratosthenes to precompute prime numbers up to `max_num`
    primes = sieve_of_eratosthenes(max_num)
    
    # Track the scores of each player
    maria_wins = 0
    ben_wins = 0

    # Play each round of the game
    for n in nums:
        # Determine the number of primes up to `n`
        prime_count = count_primes_up_to(primes, n)
        
        # If the prime count is odd, Maria wins; otherwise, Ben wins
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner based on who has more wins
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None

