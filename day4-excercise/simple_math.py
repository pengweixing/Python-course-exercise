#################################################
#  File Name:simple_math.py
#  Author: Pengwei.Xing
#  Mail: xingwei421@qq.com,pengwei.xing@igp.uu.se,xpw1992@gmail.com
#  Created Time: Thu Mar  9 13:14:40 2023
#################################################

"""
A collection of simple math operations
"""

def simple_add(a,b):
    """The sum of two numbers.

    Parameters
    ----------
    a: float
        Any real numbers 
    b: float
        Any real numbers 
    Examples
    >>>simple_add(1,1)
    2

    """
    return a+b

def simple_sub(a,b):
    """The difference of two numbers. 

    Parameters
    ----------
    a: float
        Any real numbers 
    b: float
        Any real numbers 
    Examples
    >>>simple_sub(1,1)
    0
    """
    return a-b

def simple_mult(a,b):
    """The multiplication of two numbers. 

    Parameters
    ----------
    a: float
        Any real numbers 
    b: float
        Any real numbers 
    Examples
    >>>simple_mult(1,1)
    1
    """
    return a*b

def simple_div(a,b):
    """The division of two numbers. 

    Parameters
    ----------
    a: float
        Any real numbers 
    b: float
        Any real numbers except 0
    Examples
    >>>simple_div(1,1)
    1
    """
    return a/b

def poly_first(x, a0, a1):
    """a1 times x plus a0

    Parameters
    ----------
    x: float
        Any real numbers 
    a0: float
        Any real numbers
    a1: float
        Any real numbers
    Examples
    >>>poly_first(1,1,1)
    2
    """
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    """ the result from poly_first plus a2 times the square of x

    Parameters
    ----------
    x: float
        Any real numbers 
    a0: float
        Any real numbers
    a1: float
        Any real numbers
    a2: float
        Any real numbers
    Examples
    >>>poly_first(1,1,1,1)
    3
    """
    return poly_first(x, a0, a1) + a2*(x**2)

# Feel free to expand this list with more interesting mathematical operations...
# .....
