from itertools import *


k = 0
for i in permutations('кабинет'):
    print(i)
    word = ''.join(i)
    if word[-1] not in 'аие':
        k += 1
print(k)