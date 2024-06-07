from itertools import *
k = 0
for i in product('аворт', repeat=6):
    word = ''.join(i)
    k += 1
    if word == 'ворота':
        print(k)
        break