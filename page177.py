import random


class Square:
    square_list = []

    def __init__(self, h, w):
        self.height = h
        self.width = w
        self.square_list.append((self.height, self.width))
        print("{} by {} by {} by {}".format(
            self.height, self.width, self.height, self.width))


def makeSquare(x):
    for i in range(x):
        h = random.randint(1, 30)
        w = random.randint(2, 18)
        square = Square(h, w)


makeSquare(1)
