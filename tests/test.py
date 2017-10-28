
"""This module is just a test for python """

import inspect


def main():
    """Prints Hello World"""
    print "Hello World"


def getMainSource():
    """Prints mains source code"""
    print inspect.getsource(main)


if __name__ == "__main__":
    main()
