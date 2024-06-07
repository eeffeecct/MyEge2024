from itertools import *
k = 0
for w in product('авдйлстшыью', repeat=5):
    k += 1
    word = ''.join(w)
    s = ''
    for i in w:
        if i in 'аю':
            s += 'г'
        elif i not in s:
            s += 'с'

    data = set(s)
    if word[0] != 'т' or word[0] != 'ю' and word.count('г') <= 2 and \
            len(data) == len(word):
        print(k)