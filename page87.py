# Create a list
musician_list = ['blink-182', 'NOFX', 'mxpx']

# Create tuples and a list for them.
tokyo_sta = (35.681236, 139.767125)
penn_sta = (40.750568, -73.993519)
cyber_hub = (28.494071, 77.08855)
geo_list = [tokyo_sta, penn_sta, cyber_hub]

# Create a dict.
my_fav = {
    'height': 170,
    'fav_color': 'green',
    'fav_author': 'Tomihiko Morimi'
}

musician_dict = {
    'blink182': [
        'Dammit',
        'Dumpweed',
        'Wasting time'
    ],
    'NOFX': [
        'Longest line',
        'Linoleum',
        'Bob'
    ],
    'mxpx': [
        'Move to Bremerton',
        "Tomorrow's another day"
    ]
}

# Creat a program.


def quetion():
    num = input('What do you want to know about me?: ')
    try:
        if num in my_fav:
            print(my_fav[num])
        else:
            print('Oops.')
    except ValueError:
        print('Invalid Error.')


quetion()
print(musician_dict)


# Learn SET type
s = {1, 2, 3, 3, 3, 3, 4, 4, 4, 5, 1, 3, 5}
print(s)
print(type(s))
