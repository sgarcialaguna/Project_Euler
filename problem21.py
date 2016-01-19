# coding: utf-8
"""Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000."""

sumOfDivisors = {}


def sum_of_divisors(n):
    divisors = [1]
    for i in range(2, int(n / 2) + 1):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors)


for i in range(1, 10000):
    sumOfDivisors[i] = sum_of_divisors(i)

amicableNumbers = set()
for k, v in sumOfDivisors.items():
    if v >= 10000:
        continue
    if sumOfDivisors[v] == k and k != v:
        amicableNumbers.add(k)
        amicableNumbers.add(v)

print(sum(amicableNumbers))

assert sum_of_divisors(1) == 1
assert sum_of_divisors(2) == 1
assert sum_of_divisors(3) == 1
assert sum_of_divisors(4) == 3
assert sum_of_divisors(220) == 284
assert sum_of_divisors(284) == 220
