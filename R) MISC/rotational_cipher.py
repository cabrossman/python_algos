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

    output = ''
    for char in input:
        if not char.isalnum():
            ord_adj = ord(char)
        elif char.isdigit():
            ord_adj = ord(char) - ord('0') #adjust scale to 0
            ord_adj = ord_adj + rotationFactor #add rotation factor
            ord_adj = ord_adj % 10 # modulous for decimal
            ord_adj = ord_adj + ord('0') #adjust back scale
        elif char.isupper():
            ord_adj = ord(char) - ord('A') #adjust scale to 0
            ord_adj = ord_adj + rotationFactor #add rotation factor
            ord_adj = ord_adj % 26 # modulous for letters
            ord_adj = ord_adj + ord('A') #adjust back scale
        else:
            ord_adj = ord(char) - ord('a') #adjust scale to 0
            ord_adj = ord_adj + rotationFactor #add rotation factor
            ord_adj = ord_adj % 26 # modulous for letters
            ord_adj = ord_adj + ord('a') #adjust back scale

        output = output + chr(ord_adj)

    return output



assert rotationalCipher('Zebra-493?', 3) == 'Cheud-726?'
assert rotationalCipher('abcdefghijklmNOPQRSTUVWXYZ0123456789', 39) == 'nopqrstuvwxyzABCDEFGHIJKLM9012345678'
assert rotationalCipher('All-convoYs-9-be:Alert1.', 4) == 'Epp-gsrzsCw-3-fi:Epivx5.'