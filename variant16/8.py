from itertools import *
k = 0
for i in product('адуч', repeat=5):
    w = ''.join(i)
    if w[0] in 'ау':
        k += 1
        if w == 'удача':
            print(k)
        