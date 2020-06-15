import random
word_list = ['blink', 'greenday', 'mxpx', 'nofx', 'offspring']
i = random.randint(0, 4)


def hangman(word):
    wrong = 0
    stages = [
        "",
        "_________          ",
        "|                  ",
        "|        |         ",
        "|        0         ",
        "|       /|\        ",
        "|       / \        ",
        "|                  "
    ]

    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print('Welcome to Hangman.')
    while wrong < len(stages) - 1:
        print('\n')
        msg = 'Guess the word.'
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print('\n'.join(stages[0:e]))
        if "_" not in board:
            print('You win!')
            print(" ".join(board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0:wrong + 1]))
        print('You lose. The answer is {}.'.format(word))


hangman(word_list[i])
