"""The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million."""

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
    print(longest_collatz_sequence)


find_longest_collatz_sequence()
