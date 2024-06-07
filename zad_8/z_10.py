# Маша составляет 6-значные числа в 10-ичной системе счисления. Цифры в числе не должны повторяться, и никакие две
# четные или две нечетные цифры не должны стоять рядом. Сколько чисел может составить Маша?

from itertools import *

k = 0
for w in permutations('0123456789', r=6):
    word = ''.join(w)
    for i in w:
        if i in '24680':
            word += 'c'
        else:
            word += 'n'
    if word[0] != '0' and word.count('cc') == 0 and word.count('nn') == 0:
        k += 1
print(k)
