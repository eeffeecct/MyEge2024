from itertools import *
k = 0
for i in product('0123456789', repeat=6):
    w = ''.join(i)
    s = ''
    for j in w:
        if j in '02468':
            s += 'c'
        else: 
            s += 'n'
    s1 = set(w)
    if w[0] != '0' and int(w) % 5 == 0 and 'ccnn' not in s and 'nncc' not in s and len(s1) == len(w):
        k += 1
print(k)
