import math
from collections import Counter


def prime_sieve(n):
    is_prime = [False, False] + [True] * (n - 1)
    for i in range(2, int(math.sqrt(n) + 1)):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [idx for idx, i in enumerate(is_prime) if i]


small_primes = prime_sieve(10000000)


def prime_factorization(n):
    if n == 1:
        return [1]
    primes = []
    i = 0
    while n > 1:
        if n % small_primes[i] == 0:
            primes.append(small_primes[i])
            n /= small_primes[i]
        else:
            i += 1
    return primes


def numberofdivisors(n):
    if n == 1:
        return 1
    pf = prime_factorization(n)
    lookup = Counter(pf)
    numDivisors = 1
    for val in lookup.values():
        numDivisors *= (val + 1)
    return numDivisors


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
assert (numberofdivisors(1) == 1)
assert (numberofdivisors(2) == 2)
assert (numberofdivisors(3) == 2)
assert (numberofdivisors(4) == 3)
assert (numberofdivisors(5) == 2)
assert (numberofdivisors(6) == 4)
assert (numberofdivisors(7) == 2)
assert (numberofdivisors(8) == 4)
assert (numberofdivisors(9) == 3)
assert (numberofdivisors(10) == 4)
assert (numberofdivisors(100) == 9)

if __name__ == '__main__':
    n = 1
    while True:
        triangle = (n * (n + 1)) / 2

        if numberofdivisors(triangle) >= 500:
            print triangle
            break
        n += 1