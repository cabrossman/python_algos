"""
    Signature
    string rotationalCipher(string input, int rotationFactor)

    Input
    1 <= |input| <= 1,000,000
    0 <= rotationFactor <= 1,000,000

    Output
    Return the result of rotating input a number of times equal to rotationFactor.
"""

def rotationalCipher(input, rotationFactor):
    out = ''
    for s in input:
        if not s.isalnum():
            m = ord(s)
        elif s.isdigit():
            m = ord(s) - ord('0')
            m = m + rotationFactor
            m = m % 10
            m = m + ord('0')
        elif s.isupper():
            m = ord(s) - ord('A')
            m = m + rotationFactor
            m = m % 26
            m = m + ord('A')
        elif s.islower():
            m = ord(s) - ord('a')
            m = m + rotationFactor
            m = m % 26
            m = m + ord('a')
        out = out + chr(m)
    return out

assert rotationalCipher('Zebra-493?', 3) == 'Cheud-726?'
assert rotationalCipher('abcdefghijklmNOPQRSTUVWXYZ0123456789', 39) == 'nopqrstuvwxyzABCDEFGHIJKLM9012345678'
assert rotationalCipher('All-convoYs-9-be:Alert1.', 4) == 'Epp-gsrzsCw-3-fi:Epivx5.'
print('all tests passed!')