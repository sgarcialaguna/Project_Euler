"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
 we can see that the 6th prime is 13.

What is the 10 001st prime number?"""

import primes

i = 2
known_primes = []
while len(known_primes) <= 10000:
    if primes.is_prime(i):
        known_primes.append(i)
    i += 1
print(known_primes[-1])
