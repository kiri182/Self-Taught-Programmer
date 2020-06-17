class Shape():
    def __init__(self):
        pass

    def what_am_i(self):
        print('I am a shape.')


class Rectangle(Shape):
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def calculate_perimeter(self):
        return (self.length * 2 + self.width * 2)


class Square(Shape):
    def __init__(self, s):
        self.side = s

    def calculate_perimeter(self):
        return (self.side * 4)

    def change_size(self, c):
        self.side = self.side + int(c)


class Horse():
    def __init__(self, n, c, o):
        self.name = n
        self.color = c
        self.owner = o


class Rider():
    def __init__(self, n):
        self.name = n


rider = Rider('Tom Delonge')
horse = Horse('Deep Impact', 'Black', rider)

print(horse.owner.name)
