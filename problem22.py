# coding: utf-8

"""Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand
first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name score.
For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?"""


def namescore(name):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    score = 0
    for letter in name:
        score += alphabet.index(letter) + 1
    return score


with open('p022_names.txt') as f:
    names = f.read().replace('"', '').split(',')
    names = sorted(names)

scoreSum = 0
for i, name in enumerate(names, start=1):
    scoreSum += i * namescore(name)
print(scoreSum)

assert namescore('COLIN') == 53, namescore('COLIN')
