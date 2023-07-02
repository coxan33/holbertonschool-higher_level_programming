#!/usr/bin/python3
"""Task 2"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
            Return the area of the rectangle
        """
        return self.__height * self.__width

    def display(self):
        """
            prints a representation of the rectangle
        """
        if self.__width != 0 and self.__height != 0:
            result = ""
            if self.__y > 0:
                for x in range(0, self.__y):
                    result += "\n"
            for x in range(0, self.__height):
                for y in range(0, self.__x):
                    result += " "
                result += "#" * self.__width
                if x != self.__height - 1:
                    result += "\n"
            print(result)
        else:
            print()

    def __str__(self):
        """
        This function is called when you want to print the class
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "\
            f"{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """
        This method is used by update dates of the class
        """
        if args:
            if len(args) > 4:
                self.__y = args[4]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 2:
                self.__height = args[2]
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 0:
                self.id = args[0]
        else:
            for i in kwargs:
                if i == 'height':
                    self.__height = kwargs[i]
                elif i == 'width':
                    self.__width = kwargs[i]
                elif i == 'x':
                    self.__x = kwargs[i]
                elif i == 'y':
                    self.__y = kwargs[i]
                elif i == 'id':
                    self.id = kwargs[i]

    def to_dictionary(self):
        """
        That method returns the dictionary representation of a Rectangle
        """
        return {'id': self.id, 'width': self.__width,
                'height': self.__height, 'x': self.__x, 'y': self.__y}
