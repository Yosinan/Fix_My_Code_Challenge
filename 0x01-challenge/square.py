#!/usr/bin/python3
'''
Square Module

'''


class Square():
    ''' class that defines a square '''

    def __init__(self, width=0, height=0):
        ''' init method '''
        self.width = width
        self.height = height

    @property
    def width(self):
        ''' getter for width '''
        return self.__width

    @property
    def height(self):
        ''' getter for height '''
        return self.__height

    @width.setter
    def width(self, val):
        ''' setter for width '''
        if val < 1:
            raise ValueError('Width can not be less than 1')
        else:
            self.__width = val

    @height.setter
    def height(self, val):
        ''' setter for height '''
        if val < 1:
            raise ValueError('Height can not be less than 1')
        else:
            self.__height = val

    '''
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    '''

    def area_of_my_square(self):
        """ Area of the square """
        return (self.width * self.height)

    def PermiterOfMySquare(self):
        ''' perimeter of square '''
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        ''' str rep of the square '''
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
