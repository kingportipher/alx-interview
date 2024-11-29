#!/usr/bin/python3

def isWinner(x, nums):
    """Determine the winner of the prime game played by Maria and Ben."""
    maria_score = 0
    ben_score = 0

    # Play each game round based on the numbers in `nums`
    for num in nums:
        # Create a list of all integers from 1 to `num`
        available_numbers = list(range(1, num + 1))
        # Identify all prime numbers within the range
        primes = get_primes(1, num)

        # If there are no prime numbers, Ben wins the round
        if not primes:
            ben_score += 1
            continue

        # Start the game with Maria's turn
        maria_turn = True
        while True:
            # If no primes are left, determine the winner of the current round
            if not primes:
                if maria_turn:
                    ben_score += 1
                else:
                    maria_score += 1
                break

            # Pick the smallest prime, remove it and its multiples
            smallest_prime = primes.pop(0)
            available_numbers.remove(smallest_prime)
            available_numbers = [n for n in available_numbers if n % smallest_prime != 0]

            # Switch turns
            maria_turn = not maria_turn

    # Determine the overall winner based on the scores
    if maria_score > ben_score:
        return "Winner: Maria"
    if ben_score > maria_score:
        return "Winner: Ben"
    return None

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_primes(start, end):
    """Retrieve a list of prime numbers within a specified range."""
    return [num for num in range(start, end + 1) if is_prime(num)]

