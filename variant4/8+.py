from itertools import *
k = 0
for w in product('0123456', repeat=5):
    word = ''.join(w)
    even = []
    odd = []
    for i in word:
        if i in '246':
            even.append(int(i))
        else:
            odd.append(int(i))

    if word.count('6') == 1 and sum(even) < sum(odd) and word[0] != '0':
        k += 1
print(k)