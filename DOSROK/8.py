from itertools import *

k = 0
for i in product('апрсу', repeat=5):
    k += 1
    word = ''.join(i)
    if word.count('у') <= 1 and 'аа' not in word:
        print(k)
        break
