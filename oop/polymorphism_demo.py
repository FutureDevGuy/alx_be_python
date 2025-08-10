#!/usr/bin/env python3
import math

class Shape:
    """
    A base class for all shapes.
    It defines a common interface for calculating the area.
    """
    def area(self):
        """
        Calculates the area of the shape.
        This method is a placeholder and must be overridden by derived classes.
        """
        raise NotImplementedError("Subclass must implement abstract method 'area'")


class Rectangle(Shape):
    """
    A derived class representing a rectangle.
    It inherits from Shape and provides its own implementation of the area() method.
    """
    def __init__(self, length, width):
        """
        Initializes the Rectangle with a length and a width.
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Overrides the area method to calculate the area of the rectangle.
        Formula: length * width
        """
        return self.length * self.width


class Circle(Shape):
    """
    A derived class representing a circle.
    It inherits from Shape and provides its own implementation of the area() method.
    """
    def __init__(self, radius):
        """
        Initializes the Circle with a radius.
        """
        self.radius = radius

    def area(self):
        """
        Overrides the area method to calculate the area of the circle.
        Formula: π * radius^2
        """
        return math.pi * (self.radius ** 2)
