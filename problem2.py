def fib(n):
    if n == 0:
        return 1

    if n == 1:
        return 2

    return fib(n-1) + fib(n-2)

if __name__ == '__main__':
    sum = 0
    for i in range(1, 1000000):
        f = fib(i)

        if f > 4000000:
            break

        if f %2 == 0:
            sum += f

    print sum
