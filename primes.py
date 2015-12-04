import math


def prime_factorization(n):
    if n < 1:
        raise NotImplemented
    if n == 1:
        return [1]
    primeFactors = []
    i = 2
    while i * i <= n:
        if n % i != 0:
            i += 1
        else:
            n //= i
            primeFactors.append(i)
    if n > 1:
        primeFactors.append(n)
    return primeFactors


def is_prime(n):
    return len(prime_factorization(n)) == 1


def prime_sieve(n):
    is_prime = [False, False] + [True] * (n - 1)
    for i in range(2, int(math.sqrt(n) + 1)):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [idx for idx, i in enumerate(is_prime) if i]


assert (prime_factorization(1) == [1])
assert (prime_factorization(2) == [2])
assert (prime_factorization(3) == [3])
assert (prime_factorization(4) == [2, 2])
assert (prime_factorization(5) == [5])
assert (prime_factorization(6) == [2, 3])
assert (prime_factorization(7) == [7])
assert (prime_factorization(8) == [2, 2, 2])
assert (prime_factorization(9) == [3, 3])
assert (prime_factorization(10) == [2, 5])
assert (prime_factorization(100) == [2, 2, 5, 5])
