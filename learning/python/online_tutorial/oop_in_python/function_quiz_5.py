"""
Rewrite the calculator function from exercise 4 so that it takes any number of number parameters as well as the same optional keyword parameters. The function should apply the operation to the first two numbers, and then apply it again to the result and the next number, and so on. For example, if the numbers are 6, 4, 9 and 1 and the operation is subtraction the function should return 6 - 4 - 9 - 1. If only one number is entered, it should be returned unmodified. If no numbers are entered, raise an exception.
"""

import math

ADD, SUB, MUL, DIV = range(4)

def calculator(a, b, operation=ADD, output_format=float):
    if operation == ADD:
        result = a + b
    elif operation == SUB:
        result = a - b
    elif operation == MUL:
        result = a * b
    elif operation == DIV:
        result = a / b
    else:
        raise ValueError("Operation must be ADD, SUB, MUL or DIV.")

    if output_format == float:
        result = float(result)
    elif output_format == int:
        result = math.round(result)
    else:
        raise ValueError("Format must be float or int.")

    return result