#!/usr/bin/python3
"""Task 10"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(height=size, width=size, x=x, y=y, id=id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """
        This function is called when you want to print the class
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """
        This method is used by update dates of the class
        """
        if args:
            if len(args) > 3:
                self.y = args[3]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 1:
                self.width = args[1]
                self.height = args[1]
            if len(args) > 0:
                self.id = args[0]
        else:
            for i in kwargs:
                if i == 'size':
                    self.height = kwargs[i]
                    self.width = kwargs[i]
                elif i == 'x':
                    self.x = kwargs[i]
                elif i == 'y':
                    self.y = kwargs[i]
                elif i == 'id':
                    self.id = kwargs[i]

    def to_dictionary(self):
        """
        That method returns the dictionary representation of a Square
        """
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
