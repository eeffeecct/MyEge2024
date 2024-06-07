from itertools import * 
k = 0
for i in product('_*', repeat=6):
    word = ''.join(i)
    k += 1
print(k)