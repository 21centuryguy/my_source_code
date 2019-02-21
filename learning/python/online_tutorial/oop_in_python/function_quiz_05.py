import math

ADD, SUB, MUL, DIV = range(4)

def calculator(operation=ADD, output_format=float, *args):
    if not args:
        raise ValueError("At least one number must be entered.")

    result = args[0]

    for n in args[1:]:
        if operation == ADD:
            result += n
        elif operation == SUB:
            result -= n
        elif operation == MUL:
            result *= n
        elif operation == DIV:
            result /= n
        else:
            raise ValueError("Operation must be ADD, SUB, MUL or DIV.")

    if output_format == float:
        result = float(result)
    elif output_format == int:
        result = math.round(result)
    else:
        raise ValueError("Format must be float or int.")

    return result

print(calculator(operation=ADD, output_format=float, *args))

