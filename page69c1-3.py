def square(x):
    return x ** 2


def strings(x):
    print(x)


def func(x, y, z, i=10, j=2):
    print(x)
    print(y)
    print(z)
    if i > 1:
        print(i)
    else:
        print(j)


i = input("what number do you like?: ")
print(square(int(i)))

strings('Btw, how are you?')

func('a', 'b', 'c', 5)
