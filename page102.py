def camus():
    camus_list = 'カミュ'
    for i in range(len(camus_list)):
        print(camus_list[i])


def format_str():
    what1 = input('入力1: ')
    what2 = input('入力2: ')
    result = '私は昨日{}を書いて、{}に送った'.format(what1, what2)
    print(result)


def cap():
    result = 'aldous Huxley was born in 1894.'.capitalize()
    print(result)


def fox():
    str_list = ['The', 'fox', 'jumped', 'over', 'the', 'fence', '.']
    result = ' '.join(str_list)
    result = result[0:-2] + '.'
    print(result)


def rep():
    st = 'A screaming comes across the sky.'
    print(st.replace('s', '$'))


def hem():
    print('Hemingway'.index('m'))


def sli():
    moji = '四月の晴れた寒い日で、時計がどれも十三時を打っていた。'
    print(moji[:11])
