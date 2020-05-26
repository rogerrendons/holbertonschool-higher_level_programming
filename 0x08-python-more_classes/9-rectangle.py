#!/usr/bin/python3
""" empty class Rectangle that defines a rectangle """


class Rectangle:
    """ class Rectangle """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ initializes sizes """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ getter width """
        return self.__width

    @property
    def height(self):
        """ getter height """
        return self.__height

    @width.setter
    def width(self, value):
        """ set width """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """ set height """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """ return area """
        return (self.width * self.height)

    def perimeter(self):
        """ return perimeter """
        if self.width * self.height == 0:
            return (0)
        return ((self.width + self.height) * 2)

    def __str__(self):
        """ Rectangle Print """
        prn = ""
        if self.__width == 0 or self.__height == 0:
            return ("")
        if self.__width and self.__height:
            prn = prn + (str(self.print_symbol) * self.__width + '\n')\
                 * (self.__height - 1)
            prn = prn + str(self.print_symbol) * self.__width
        return (prn)

    def __repr__(self):
        """ Representation of rectangle. """
        return 'Rectangle({:d}, {:d})'.format(self.__width, self.__height)

    def __del__(self):
        """ Delete rectangle  """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Return if bigger or equal  """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """ returns a equal Rectangle """
        return cls(size, size)
