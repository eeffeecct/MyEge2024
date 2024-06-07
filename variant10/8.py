from itertools import *

k = 0

for w in product('012345678', repeat=5):
    word = ''.join(w)    
    if word[0] != '0' and word.count('3') == 1 and '35' not in word and '53' not in word and '36' not in word and '63' not in word and '37' not in word and '73' not in word and '38' not in word and '83' not in word: 
        k += 1
print(k)
