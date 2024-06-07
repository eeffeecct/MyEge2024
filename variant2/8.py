from itertools import *
k = 0
for i in product('авелрфь', repeat=6):
    word = ''.join(i)
    k += 1
    if 'а' not in word and 'е' not in word:
        print(k)
        break