from itertools import *
k = 0
res = 0
for i in product('аинптця',repeat=6):
    k += 1
    word = ''.join(i)
    if k % 2 == 0 and word[0] != 'н' and word.count('я') == 2:
        res += 1
print(res)