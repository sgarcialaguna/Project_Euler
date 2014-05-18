def collatz_sequence(n):
    sequence = [n]
    while sequence[-1] != 1:
        if sequence[-1] in collatz_sequence.known_sequences:
            result = len(sequence) + collatz_sequence.known_sequences[sequence[-1]] - 1
            collatz_sequence.known_sequences[n] = result
            return result
        if sequence[-1] % 2 == 0:
            sequence.append(sequence[-1] / 2)
        else:
            sequence.append(3 * sequence[-1] + 1)
    result = len(sequence)
    collatz_sequence.known_sequences[n] = result
    return result


collatz_sequence.known_sequences = {}

assert (collatz_sequence(1) == 1)
assert (collatz_sequence(13) == len([13, 40, 20, 10, 5, 16, 8, 4, 2, 1]))


def find_longest_collatz_sequence():
    global longest_collatz_sequence, i, c
    longest_collatz_sequence = (1, 1)
    for i in range(2, 1000000):
        c = collatz_sequence(i)
        if c > longest_collatz_sequence[1]:
            longest_collatz_sequence = (i, c)
    assert(longest_collatz_sequence == (837799, 525))
    print longest_collatz_sequence


import timeit
print timeit.timeit(find_longest_collatz_sequence, number=1)
