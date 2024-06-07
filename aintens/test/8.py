from itertools import *
k = 0
for i in product('0123456789', repeat=4):
    s = ''.join(i)

    if s[0] != '0' and ((s[0] == s[1] and s[1] != s[2] and s[2] != s[3]) or \
                        (s[0] != s[1] and s[1] == s[2] and s[2] != s[3]) or \
                        (s[0] != s[1] and s[1] != s[2] and s[2] == s[3])):
        k += 1
print(k)
