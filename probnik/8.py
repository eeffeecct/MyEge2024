from itertools import product

k = 0
for w in product('векорт', repeat=6):
    k += 1
    word = ''.join(w)
    if (word[0] != 'т' or word[0] != 'р') and word.count('о') == 2 and word.count('т') <= 1:
        print(k)
