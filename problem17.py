def numberToWord(n):
    word = ''
    if n == 1000:
        return 'one thousand'
    if n >= 100:
        word += numberToWord.lookup[n / 100] + ' hundred'
        remainder = numberToWord(n % 100)
        if remainder:
            word += ' and ' + remainder
        return word
    if n / 10 < 2:
        return numberToWord.lookup[n]
    word = numberToWord.lookup[n / 10 * 10]
    if n % 10 != 0:
        word += '-' + numberToWord.lookup[n % 10]
    return word


numberToWord.lookup = {0: '',
                       1: 'one',
                       2: 'two',
                       3: 'three',
                       4: 'four',
                       5: 'five',
                       6: 'six',
                       7: 'seven',
                       8: 'eight',
                       9: 'nine',
                       10: 'ten',
                       11: 'eleven',
                       12: 'twelve',
                       13: 'thirteen',
                       14: 'fourteen',
                       15: 'fifteen',
                       16: 'sixteen',
                       17: 'seventeen',
                       18: 'eighteen',
                       19: 'nineteen',
                       20: 'twenty',
                       30: 'thirty',
                       40: 'forty',
                       50: 'fifty',
                       60: 'sixty',
                       70: 'seventy',
                       80: 'eighty',
                       90: 'ninety'}

assert (numberToWord(1) == 'one')
assert (numberToWord(2) == 'two')
assert (numberToWord(3) == 'three')
assert (numberToWord(4) == 'four')
assert (numberToWord(5) == 'five')
assert (numberToWord(6) == 'six')
assert (numberToWord(7) == 'seven')
assert (numberToWord(8) == 'eight')
assert (numberToWord(9) == 'nine')
assert (numberToWord(10) == 'ten')
assert (numberToWord(11) == 'eleven')
assert (numberToWord(12) == 'twelve')
assert (numberToWord(13) == 'thirteen')
assert (numberToWord(14) == 'fourteen')
assert (numberToWord(15) == 'fifteen')
assert (numberToWord(16) == 'sixteen')
assert (numberToWord(17) == 'seventeen')
assert (numberToWord(18) == 'eighteen')
assert (numberToWord(19) == 'nineteen')
assert (numberToWord(20) == 'twenty')
assert (numberToWord(21) == 'twenty-one')
assert (numberToWord(56) == 'fifty-six')
assert (numberToWord(98) == 'ninety-eight')
assert (numberToWord(100) == 'one hundred')
assert (numberToWord(156) == 'one hundred and fifty-six')
assert (numberToWord(198) == 'one hundred and ninety-eight')
assert (numberToWord(342) == 'three hundred and forty-two')
assert (numberToWord(574) == 'five hundred and seventy-four')
assert (numberToWord(1000) == 'one thousand')

total_length = 0
for i in range(1, 1001):
    total_length += len(numberToWord(i).replace(' ', '').replace('-', ''))
print total_length
