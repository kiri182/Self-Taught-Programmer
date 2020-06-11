
def listprint():
    list_a = ['ウォーキング・デッド', 'アントラージュ', 'ザ・ソプラノズ', 'ヴァンパイア・ダイアリーズ']
    for x in list_a:
        print(x)


def count():
    for i in list(range(25, 51, 1)):
        print(i)


def loop():
    n = 0
    question = ['Who are you', 'Where are you from', "What's that"]

    while True:
        print("Hey...")
        user_input = input(question[n])
        if user_input == 'q':
            break
        n = (n + 1) % 3


def looploop():
    list1 = [8, 19, 148, 4]
    list2 = [9, 1, 33, 83]
    result = []
    i = 0
    j = 0
    k = 0

    for i in list1:
        for j in list2:
            if k < 4:
                x = i * j
                result.append(x)
                k = k + 1
        k = 0

    print(result)
