def one(i):
    return i // 2


def two(i):
    return i * 4


number = input('Please type the number you like: ')
var = one(int(number))
print(two(var))
