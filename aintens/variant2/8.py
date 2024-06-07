from itertools import *

k = 0
for x in product('0123456789abcde', repeat=5):
    s = ''.join(x)
    s1 = ''
    for i in s:
        if i in '13579':
            s1 += 'n'
        elif i in 'bd':
            s1 += 'nn'
        elif i in 'ace':
            s1 += 'cc'
        else: 
            s1 += 'c'
    if s[0] != '0' and s[-1] in '13579bd' and \
        ('0' in s or 'a' in s) and \
        'nncc' not in s1 and 'ccnn' not in s1:
        k += 1
print(k)
        

