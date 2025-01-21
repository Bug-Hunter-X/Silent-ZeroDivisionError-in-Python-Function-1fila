def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None

# This function works fine if b is not 0, but if b is 0 it prints the error message
# and returns None. This can be easily missed by the developer who assumes that the
# function always returns a numerical result.