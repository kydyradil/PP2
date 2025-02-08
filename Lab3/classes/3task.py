class Shape:
    def __init__(self):
        """  """
        pass

    def area(self):
        """  """
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        """  """
        super().__init__()  
        self.length = length
        self.width = width

    def area(self):
        """  """
        return self.length * self.width


length = float(input(" write length: "))
width = float(input(" write width:"))


rectangle = Rectangle(length, width)
print("Area of rectangle:", rectangle.area())
