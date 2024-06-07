from itertools import *

k = 0
for i in product('галкти', repeat=8):
    word = ''.join(i)
    if word[0] in 'глкт' and word[-1] in 'аи' and 'кл' not in word:
        k += 1
print(k)