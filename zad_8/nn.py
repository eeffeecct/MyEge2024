from itertools import *

k = 0
for x in permutations('012345678', r=5):
    s = ''.join(x)
    if s.count('5') == 1 and '00' not in s and '11' not in s and '22' not in s \
            and '33' not in s and '44' not in s and '55' not in s and '66' not in s \
            and '77' not in s and '88' not in s:
        k += 1
print(k)

