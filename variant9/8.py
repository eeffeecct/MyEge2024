from itertools import *

k = 0
for x in combinations(range(15, -1, -1), r = 15):
    for j in range(0, 14):
        if not(x[j] > x[j+1] and x[j] % 2 != x[j+1] % 2):
            break
    else:
        k += 1
        print(x)
    
print(k)

