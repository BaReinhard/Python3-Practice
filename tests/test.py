"""Simple Math for Testing Python3"""
import functools


def check_non_zero(index):
    """Allows for dynamic index to check checked"""
    def validator(func):
        """Decorator method providing a wrapper to check for non-zero args"""
        @functools.wraps(func)
        def wrap(*args, **kwargs):
            """Checks args at index to be non-zero"""
            if args[index] == 0:
                raise ValueError("Argument {} must not be zero".format(index))
            return func(*args, **kwargs)
        return wrap
    return validator


def factorial_recursive(num):
    """Returns Factorial of num given"""
    if num == 1:
        return num
    else:
        return num * factorial(num - 1)


@check_non_zero(0)
def factorial(num):
    """Returns Factorial of num given iteratively"""
    total = 1
    for i in range(1, num + 1):
        total *= i
    return total


def fibonacci(num):
    """Returns Fibonacci Sequence up to num numbers"""
    seq = []
    prev = 0
    current = 1
    while len(seq) != num:
        fibnum = prev + current
        seq.append(fibnum)
        prev = current
        current = fibnum
    return seq


def add(first, second):
    """Adds the first and second number together"""
    return first + second


def subtract(first, second):
    """Subtracts the second from the first"""
    return first - second


@check_non_zero(1)
def divide(first, second):
    """Divides first by second and ensures second != zero"""
    return first / second
