#!/usr/bin/python3
"""
    contains class Square implements class Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Square implements rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
            initialises Square (overrides Rectangle init)
        """
        super().__init__(size, size, x, y, id)
        self.__size = size
        self.__x = x
        self.__y = y

    def __str__(self):
        """
            returns the size of the square
        """
        return ("[{}] ({}) {}/{} - {}"
                .format(type(self).__name__, self.id, self.__x, self.__y, self.__size))

    @property
    def size(self):
        """
            returns the size of the square
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
            sets the value of size
        """
        if type(size) != int:
            raise TypeError("width must be an integer")
        elif size <= 0:
            raise ValueError("width must be > 0")
        self.__width = size
        self.__height = size
        self.__size = size

    def update(self, *args, **kwargs):
        """
            assigns key/value argument to attributes
            kwargs is skipped if args is not empty
            Args:
                *args -  variable number of no-keyword args
                **kwargs - variable number of keyworded args
        """
        if args:
            try:
                self.id = args[0]
                self.__size = args[1]
                self.__x = args[2]
                self.__y = args[3]
            except:
                pass
        else:
            self.id = kwargs.get('id', self.id)
            self.__size = kwargs.get('size', self.__size)
            self.__x = kwargs.get('x', self.__x)
            self.__y = kwargs.get('y', self.__y)

    def to_dictionary(self):
        """
            Returns the dictionary representation of a Square
        """
        s = {'id': self.id, 'x': self.__x, 'size': self.__size, 'y': self.__y}
        return s
