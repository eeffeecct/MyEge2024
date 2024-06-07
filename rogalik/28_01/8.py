from itertools import *


k = 0
n = 0

for k in range(1, 100000):
    if k % 5 == 0:
        continue
    else:
        for i in product('авикпрчы', repeat=5):
            word = ''.join(i)
            if 'вкпрчы' in word:
                print(i)
                break


