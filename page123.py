import statistics
import random
import cubed


def math():
    num_list = []
    for i in (random.randint(1, 30) for j in range(10)):
        num_list.append(i)

    print(num_list)
    # mean
    print(statistics.mean(num_list))
    # median
    print(statistics.median(num_list))

    # mode
    # statistics.mode(num_list)
    print(statistics.groupby(num_list))


def triple(x):
    cubed.answer(x)


num = input('Type the number you like: ')
triple(int(num))
