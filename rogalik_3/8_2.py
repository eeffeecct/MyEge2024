from itertools import *

k = 0
for w in permutations('неверленд'):
    word = ''.join(w)
    if 'ее' not in word and 'еее' not in word:
        k += 1
        print(k)
    print(word)
print(k)
