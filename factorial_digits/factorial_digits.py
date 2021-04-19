import numpy as np

def calculate_sum_of_factorial_digits(numeric_value):
    if type(numeric_value) != int:
        raise TypeError("The factorial requires a non-negative integer.")

    if numeric_value < 0:
        raise ValueError("The input to a factorial cannot be negative.")

    factorial = np.math.factorial(numeric_value)

    return calculate_sum_of_digits(factorial)

def calculate_sum_of_digits(value):
    sum_of_digits = 0

    while value > 0:
        sum_of_digits += value % 10
        value //= 10

    return sum_of_digits
