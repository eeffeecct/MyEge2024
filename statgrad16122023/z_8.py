from itertools import *

k = 0
for x in product('012345678', repeat=5):
    s = ''.join(x)
    if s[0] != '0' and s.count('5') == 1 and s[0] != s[1] and s[1] != s[2] and s[2] != s[3] and s[3] != s[4]:
        k += 1
print(k)

# забыл проверить что нельзя на 0 начать