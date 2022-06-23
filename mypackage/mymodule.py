""" 
Simple module for docstring presentation.

Classes:

    laptop

Functions:

    simpleAdder(num1, num2)
    simpleSubtracter(num1, num2)
    simpleProductFn(num1, num2)
"""

def simpleAdder(num1, num2):
    """Takes in two numbers and returns their sum."""
    return num1 + num2

def simpleSubtracter(num1, num2):
    """Takes in two number and returns their difference.
    
    In math, to subtract means to take away from a group 
    or a number of things. When we subtract, the number 
    of things in the group reduces or becomes less. The 
    minuend, subtrahend, and difference are parts of a s
    ubtraction problem. This class subtracts num2 from num1"""
    return num1 - num2


def simpleProductFn(num1, num2):
    """
    Returns the product of two numbers.

    Parameters
    ----------
    num1 : float
        The first number to multiply
    num2 : float
        The second number to multiply

    Returns
    -------
    num_prod: float
        The product of num1 and num2
    """
    num_prod = num1 * num2
    return num_prod



class laptop:
    """
    A class to represent a laptop

    Attributes
    ----------
    brand: string
        - The brand of the laptop
    price: int
        - The price of the laptop

    Methods
    -------
    printPrice()
        - Prints the price of the laptop.
    """
    def init(self, brand, price):
        """
        Constructs all the necessary attributes for the class object.

        Parameters
        ----------
        brand : _type_
            _description_
        price : _type_
            _description_
        """
        self.brand = brand
        self.price = price

    def printPrice(self):
        """
        Prints the price of the laptop.
        """
        print(f'The price of this laptop is {self.price}')

