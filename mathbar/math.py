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

    @staticmethod
    def factorial_iterative(num):
        """Returns Factorial of number given iteratively"""
        total = 1
        for i in range(1, num + 1):
            total *= i
        return total

    @staticmethod
    def fibonacci(num):
        """Returns Fibonacci Sequence up to x numbers"""
        seq = []
        prev = 0
        current = 1
        while(len(seq) != num):
            fibnum = prev + current
            seq.append(fibnum)
            prev = current
            current = fibnum
        return seq
