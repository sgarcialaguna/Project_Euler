"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""
from collections import defaultdict, Counter

import primes

d = defaultdict(int)

for i in range(2, 21):
    pf = primes.prime_factorization(i)
    for k, v in Counter(pf).items():
        d[k] = max(d[k], v)

lcm = 1
for k, v in d.items():
    lcm *= pow(k, v)
print(lcm)
