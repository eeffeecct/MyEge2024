# Артур составляет 5-буквенные коды из букв Е, С, А, У, Л. Каждую букву нужно использовать ровно один раз,
# при этом нельзя ставить рядом две гласные. Сколько различных кодов может составить Артур?

from itertools import *

k = 0
for w in permutations('есаул', r=5):
    word = ''.join(w)
    if 'еа' not in word and 'ае' not in word and 'еу' not in word \
            and 'уе' not in word and 'ау' not in word and 'уа' not in word:
        k += 1
print(k)
