def calculator(expression):
    number = 0
    sign_value = 1
    result = 0
    operations_stack = []

    for c in expression:
        if c.isdigit():
            number = number * 10 + int(c)
        elif c in "+-":
            result += number * sign_value
            sign_value = -1 if c == '-' else 1
            number = 0
        elif c == '(':
            operations_stack.append(result)
            operations_stack.append(sign_value)
            result = 0
            sign_value = 1
        elif c == ')':
            result += sign_value * number
            pop_sign_value = operations_stack.pop()
            result *= pop_sign_value

            second_value = operations_stack.pop()
            result += second_value
            number = 0
    
    return result + number * sign_value

assert calculator("12 - (6 + 2) + 5") == 9
assert calculator("(8 + 100) + (13 - 8 - (2 + 1))") == 110
assert calculator("40 - 25 - 5") == 10