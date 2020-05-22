#!/usr/bin/python3
"""
add_integer
adds two numbers (int or float)
return int(a) + int(b)
"""
def add_integer(a, b=98):
    """
    Addition function only with integer or float input,
    and integer output
    """
    if type(a)not in [int,float] and type(a)not in [int,float]:
        raise TypeError("a must be an integer")
    elif type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")


    return int(a) + int(b)
