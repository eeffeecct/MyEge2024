from itertools import *
k = 0
for i in product('012345678', repeat=7):
    word = ''.join(i)
    if word[0] != '0' and int(word[0]) % 2 == 0 and int(word[-1]) % 2 != 0 and word.count('8') <= 1:
        k += 1
print(k)