"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""

import math

n = 600851475143


def prime_sieve(n):
    is_prime = [False, False] + [True] * (n-1)
    for i in range(2, int(math.sqrt(n) + 1)):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return [idx for idx, i in enumerate(is_prime) if i]

def trial_division(n):
    primes = prime_sieve(int(n**0.5)+ 1)
    prime_factors = []

    for p in primes:
        if n % p == 0:
            prime_factors.append(p)

    return prime_factors

if __name__ == '__main__':
    print(trial_division(n)[-1])
