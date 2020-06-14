import os
import csv

movie_list = [['Top Gun', 'Risky Business', 'Minority Report'], [
    'Tytanix', 'The Revenant', 'Inception'], ['Training Day', 'Man of Fire', 'Flight']]


def reading():
    path = input('Type your path: ')
    files = input('Which file?: ')
    with open(os.path.join(path, files), "r") as f:
        print(f.read())


def question():
    path = input('Type your path: ')
    q_answer = input('What is your fav food?: ')
    with open(os.path.join(path, 'food.txt'), 'w+') as f:
        print('Ok, I got it. Keep it in my mind.')
        f.write(q_answer)
        print(f.read())


def makecsv():
    with open('movie.csv', 'w', newline='') as f:
        w = csv.writer(f, delimiter=',')
        for i in movie_list:
            w.writerow(i)
