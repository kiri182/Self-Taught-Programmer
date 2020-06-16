import math


class Apple:
    def __init__(self, w, c, f, p):
        self.weight = w
        self.color = c
        self.farm = f
        self.price = p


class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius ** 2 * math.pi


# circle = Circle(2)
# print(circle.area())

class Triangle:
    def __init__(self, b, h):
        self.base = b
        self.height = h

    def area(self):
        return self.base * self.height * 0.5


# triangle = Triangle(2, 3)
# print(triangle.area())

class Hexagon:
    def __init__(self, s1, s2, s3, s4, s5, s6):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5
        self.s6 = s6

    def calculate_perimeter(self):
        return self.s1 + self.s2 + self.s3 + self.s4 + self.s5 + self.s6


hx = Hexagon(134, 124, 3645, 68, 24, 35)
print(hx.calculate_perimeter())
