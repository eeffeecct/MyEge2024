from itertools import *

k = 0
for w in product('гипербола', repeat=6):
    word = ''.join(w)
    s = ''
    for i in word:
        if i in 'гпрбл':
            s += 's'
        else:
            s += 'g'
    if s[0] != 'g' and s[-1] != 'g' and 'sgs' not in s:
        k += 1
print(k)
