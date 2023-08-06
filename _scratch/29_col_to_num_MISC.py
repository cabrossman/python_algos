def convertToInt(COLS):
    total = 0
    for i, c in enumerate(reversed(COLS)):
        subtot = ord(c) - ord('A') + 1
        subtot = subtot*(26**i)
        total = total + subtot
    return total

def convertToTitle(n):
    s = ''
    while n > 0:
        n -= 1
        rem = n % 26
        letter_idx = ord('A') + rem
        letter_chr = chr(letter_idx)
        s = letter_chr + s
        n = n // 26
    return s

assert convertToInt('A') == 1
assert convertToInt('AB') == 28
assert convertToInt('ZY') == 701

assert convertToTitle(1) == 'A'
assert convertToTitle(28) == 'AB'
assert convertToTitle(701) == 'ZY'
print('all tests have passed!')