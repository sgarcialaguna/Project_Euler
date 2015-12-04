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
