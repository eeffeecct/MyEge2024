from itertools import * 
k = 0
for i in product('012345678', repeat=6):
    s = ''.join(i)
    s1 = ''
    for i in s: 
        if i in '1357':
            s1 += '1'
        else: 
            s1 += i
    if s[0] != '0' and s.count('6') == 1 and '161' not in s1:
        k += 1
print(k)
