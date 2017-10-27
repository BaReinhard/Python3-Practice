"""Simple Math Class for Testing Python3"""


class Mathematics(object):
    """Simple Math Class for Testing Python3"""

    def __init__(self):
        """Inits Mathematics Class"""
        self.name = "Bar Math"
        self.type = "Function Dict"

    def factorial(self, num):
        """Returns Factorial of number given"""
        if num == 1:
            return num
        else:
            return num * self.factorial(num - 1)

    def factorial_iterative(self, num):
        """Returns Factorial of number given iteratively"""
        total = 1
        for i in range(1, num + 1):
            total *= i
        return total
