from itertools import *
k=0
for i in product('алпця', repeat=5):
    word = ''.join(i)
    k += 1
    if word.count('а') == 1 and word.count('ц') == 2 and word.count('л') == 0:
        print(k)
        break
