#!/usr/bin/python3

def is_prime(num):
  """Checks if a number is prime."""
  if num <= 1:
    return False
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
  return  
 True

def find_primes(n):
  """Finds all prime numbers up to n."""
  primes = []
  for num in range(2, n + 1):
    if is_prime(num):
      primes.append(num)
  return primes

def isWinner(x, nums):
  """Determines the winner of the game."""
  maria_wins = 0
  ben_wins = 0
  for n in nums:
    primes = find_primes(n)
    while primes:
      primes = [prime for prime in primes if not any(multiple % prime == 0 for multiple in primes)]
    if len(primes) % 2 == 0:
      ben_wins += 1
    else:
      maria_wins += 1
  if maria_wins > ben_wins:
    return "Maria"
  elif ben_wins > maria_wins:
    return "Ben"
  else:
    return None
