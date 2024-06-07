from itertools import *

k = 0
for n in product('аекптч', repeat=7):
    word = ''.join(n)
    k += 1
    if word == 'аптечка':
        ap = k
    elif word == 'печатка':
        pk = k
        print(pk - ap - 1)
        break
