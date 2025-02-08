import math

class Point:
    def __init__(self, x, y):
        """  """
        self.x = x
        self.y = y

    def show(self):
        """  """
        print(f"point with coord: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        """   """
        self.x = new_x
        self.y = new_y
        print(f"cord changed: ({self.x}, {self.y})")

    def dist(self, other_point):
        """  """
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)


x1 = float(input("write x first point: "))
y1 = float(input("write y first point: "))
point1 = Point(x1, y1)
point1.show()


x2 = float(input("write x second point: "))
y2 = float(input("write y  second point: "))
point2 = Point(x2, y2)

print(f"distance : {point1.dist(point2)}")


new_x1 = float(input("write new  x for first point: "))
new_y1 = float(input("write new y for first point: "))
point1.move(new_x1, new_y1)
