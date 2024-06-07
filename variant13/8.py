from itertools import * 
k = 0
for i in product('агдилнря', repeat=6):
    w = ''.join(i)
    k += 1
    if k % 2 == 0 and w[0] != 'я' and w.count('д') == 3: 
        print(k) 