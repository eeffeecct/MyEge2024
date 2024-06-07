from itertools import * 
k = 0
res = 0
for i in product('ажимнуч',repeat=6):
    k += 1
    s = ''.join(i)
    if s[0]!='ж' and s.count('ч') <= 1 and k % 2 == 0:
        res += 1
print(res)