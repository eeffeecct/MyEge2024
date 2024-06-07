from itertools import *
k = 0
for n in product('апрсу',repeat=5):
    k += 1
    s = ''.join(n)
    if s.count('у') <= 1 and s.count('аа') == 0:
        print(k)