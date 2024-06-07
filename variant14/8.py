from itertools import *
k = 0
for i in product('апрсу', repeat=5): 
    k += 1
    w = ''.join(i)
    if w.count('у') <= 1 and 'aa' not in w: 
        print(k)
        