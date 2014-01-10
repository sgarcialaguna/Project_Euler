# find prime factors of numbers 1 - 20 on paper
solution = 19*17*13*11*7*5*(3**2)*(2**4)
for i in range(20, 2, -1):
    assert(solution % i == 0)
print solution