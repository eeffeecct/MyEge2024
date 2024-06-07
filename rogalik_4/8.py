from itertools import *
p = 0
k = 0
for i in product('еикрсуя', repeat=6):
    k += 1
    word = ''.join(i)

    s = ''
    for i in word:
        if i in 'еиуя':
            s += 'g'
        else:
            s += 's'

    if k % 2 == 0 and word[0] != 'к' and s.count('g') <= 2:
        p += 1

print(p)