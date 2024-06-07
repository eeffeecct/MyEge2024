from itertools import *
k = 0
for n in product('абвку', repeat=7):
    w = ''.join(n)
    k += 1
    s = ''
    for i in w :
        if i in 'ау':
            s += 'g'
        else: 
            s += 's'
    if 'gg' not in s and 'ss' not in s: 
        print(k)