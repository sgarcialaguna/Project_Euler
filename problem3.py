n = 600851475143

def prime_sieve(n):
   possible_primes = range(2,n)
   is_prime = [True] * (n + 1)

   for i in possible_primes:
        if is_prime[i]:
            j = 2
            while i * j < n:
                is_prime[i * j - 2] = False
                j += 1

   primes = []
   for i in possible_primes:
       if is_prime[i - 2]:
           primes.append(i)
   return primes

def trial_division(n):
    primes = prime_sieve(int(n**0.5)+ 1)
    prime_factors = []

    for p in primes:
        if n % p == 0:
            prime_factors.append(p)

    return prime_factors

if __name__ == '__main__':
    print trial_division(n)