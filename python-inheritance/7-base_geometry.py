#!/usr/bin/python3
"""
Module for BaseGeometry class
"""


class BaseGeometry:
    """
    Base class for geometry objects
    """

    def area(self):
        """
        Public instance method that raises an Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is an integer and greater than 0

        Args:
            name (str): The name of the parameter
            value (int): The value to validate

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is <= 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
