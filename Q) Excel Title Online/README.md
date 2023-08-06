# 17. Excel Solve

## What is it?
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
Given an column title, return its corresponding integer columnNumber as it appears in an Excel sheet.

## Concepts
Python `ord()` function returns the Unicode code integer from a given character.
- `ord('A') == 65`
- `ord('Z') == 90`
Python `chr()` function returns the Unicode character from a given integer
- `chr(65) == A`
- `chr(24 + ord('A')) == 'Y'`

Python `%` returns the integer remainder when taking a larger number into a smaller 
-  `26**3 % 26 == 0`
- `9 % 5 == 4`


Let's see the relationship between the Excel sheet column title and the number:
A   1     AA    26+ 1     BA  2×26+ 1     ...     ZA  26×26+ 1     AAA  1×26²+1×26+ 1
B   2     AB    26+ 2     BB  2×26+ 2     ...     ZB  26×26+ 2     AAB  1×26²+1×26+ 2
.   .     ..    .....     ..  .......     ...     ..  ........     ...  .............   
.   .     ..    .....     ..  .......     ...     ..  ........     ...  .............
.   .     ..    .....     ..  .......     ...     ..  ........     ...  .............
Z  26     AZ    26+26     BZ  2×26+26     ...     ZZ  26×26+26     AAZ  1×26²+1×26+26

Now we can see that ABCD＝A×26³＋B×26²＋C×26¹＋D＝1×26³＋2×26²＋3×26¹＋4

But how to get the column title from the number? We can't simply use the n%26 method because:

ZZZZ＝Z×26³＋Z×26²＋Z×26¹＋Z＝26×26³＋26×26²＋26×26¹＋26

We can use (n-1)%26 instead, then we get a number range from 0 to 25.

## How its done
### Num to Char
```
def convertToTitle(num):
    caps = [chr(x) for x in range(ord('A'), ord('Z')+1)]
    result = []
    while num > 0:
        last_char_int = (num -1) % 26
        last_char = caps[last_char_int]
        result.append(last_char)
        num = (num -1) // 26
    result.reverse()
    return ''.join(result)
```

### Chr to Num
The while statement allows a flexible window size. It shrinks the window start
```
def convertToInt(COLS):
    tot = 0
    for i, col in enumerate(COLS[::-1]):
        char_int = ord(col) - ord('A') + 1
        subtotal = char_int*(26**i)
        tot = tot + subtotal
    return tot
```