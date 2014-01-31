import math


def prime_sieve(n):
    is_prime = [False, False] + [True] * (n-1)
    for i in range(2, int(math.sqrt(n) + 1)):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return [idx for idx, i in enumerate(is_prime) if i]

print sum(prime_sieve(2000000))
