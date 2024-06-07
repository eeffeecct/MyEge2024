from itertools import *
k = 0
for i in product('векорт',repeat=6):

    s = ''.join(i)
    if s[0] != 'в' and s[0] != 'е' and s.count('к') <= 3 and s.count('о') == 2:
        k += 1
print(k)