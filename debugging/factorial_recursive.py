#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer.

    Function Description:
    This function computes the factorial of a given non-negative integer `n` using recursion.
    The factorial of 0 is defined as 1, and for positive integers, it's the product of all integers from 1 to `n`.

    Parameters:
    n (int): A non-negative integer for which the factorial is to be calculated.

    Returns:
    int: The factorial of the input integer `n`.
    """
    if n == 0:  # Base case: factorial of 0 is 1
        return 1
    else:  # Recursive case: factorial(n) = n * factorial(n-1)
        return n * factorial(n-1)

# Get the input number from the command line arguments
f = factorial(int(sys.argv[1]))

# Print the result
print(f)