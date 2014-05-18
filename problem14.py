def collatz_sequence(n):
    result = [n]
    while result[-1] != 1:
        if result[-1] in collatz_sequence.known_sequences:
            result.extend(collatz_sequence.known_sequences[result[-1]][1:])
            break
        if result[-1] % 2 == 0:
            result.append(result[-1] / 2)
        else:
            result.append(3 * result[-1] + 1)
    collatz_sequence.known_sequences[n] = result
    return result


collatz_sequence.known_sequences = {}

assert (collatz_sequence(1) == [1])
assert (collatz_sequence(13) == [13, 40, 20, 10, 5, 16, 8, 4, 2, 1])


def find_longest_collatz_sequence():
    global longest_collatz_sequence, i, c
    longest_collatz_sequence = (1, 1)
    for i in range(2, 1000000):
        c = collatz_sequence(i)
        if len(c) > longest_collatz_sequence[1]:
            longest_collatz_sequence = (i, len(c))
    print longest_collatz_sequence


import timeit

print timeit.timeit(find_longest_collatz_sequence, number=1)