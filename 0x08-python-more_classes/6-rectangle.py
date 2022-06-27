#!/usr/bin/python3
"""
This module defines a Square class
Its implements value and type checks for its attributes with area function
"""


class Rectangle:
    """Square implementation
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        return (self.get_str())

    def __repr__(self):
        return 'Rectangle({0.width!r}, {0.height!r})'.format(self)

    def __eval__(self):
        return Rectangle()

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
        del self

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0

        return (2 * (self.__width + self.__height))

    def get_str(self):
        total = ""
        if self.__width == 0 or self.__height == 0:
            return total
        for i in range(self.__height):
            total += ("#" * self.__width)
            if i != (self.__height - 1):
                total += "\n"
        return total
