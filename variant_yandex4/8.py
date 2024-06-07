from itertools import *

k = 0
for i in product('аёртш', repeat=5):
    k += 1
    word = ''.join(i)
    if word.count('а') <= 1 and 'ёё' not in word: 
        print(k)
        break
