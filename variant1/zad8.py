from itertools import *

k = 0
for i in product('иклнор', repeat=4):
    word = ''.join(i)
    k += 1
    if word == 'кино':
        print(k)
        break