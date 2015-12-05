from collections import Counter

from primes import prime_factorization

def numberofdivisors(n):
    if n == 1:
        return 1
    pf = prime_factorization(n)
    lookup = Counter(pf)
    numDivisors = 1
    for val in lookup.values():
        numDivisors *= (val + 1)
    return numDivisors

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

n = 1
while True:
    triangle = (n * (n + 1)) / 2

    if numberofdivisors(triangle) >= 500:
        print(triangle)
        break
    n += 1
