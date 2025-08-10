#!/usr/bin/env python3

class Calculator:
    """
    A class to demonstrate the use of static and class methods.
    """
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        A static method to perform addition.
        It doesn't need access to class or instance state.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        A class method to perform multiplication.
        It accesses a class attribute using the 'cls' parameter.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
