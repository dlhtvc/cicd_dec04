import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    """ division by 0 """
    if b == 0:
        return None
    return a / b

def log(x, base):
    """ 
    log of x with given base.
    Returns None if x <= 0 or base <= 0 or base == 1
    """
    if x <= 0 or base <= 0  or base == 1:
        return None
    return math.log(x, base)

def square(a):
    return a ** 2

def sin(x, degrees = False):
    """ If degrees = True, x is interpreted as degrees; otherwise radians """
    if degrees: 
        x = math.radians(x)
    return math.sin(x)

def cos(x, degrees = False):
    """ If degrees = True, x is interpreted as degrees; otherwise radians """
    if degrees: 
        x = math.radians(x)
    return math.cos(x)

def square_root(x):
    """ Square root of x, or None for negative x """
    if x < 0:
        return None
    return math.sqrt(x)

def percentage(a, b):
    if b == 0:
        return None 
    return (a / b) * 100

