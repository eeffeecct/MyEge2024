# Определите количество семизначных чисел, записанных в девятеричной системе счисления, учитывая, что числа не могут
# заканчиваться на цифры 3, 4 и 7 и не должны содержать тройки соседних одинаковых цифр (например, 000).

from itertools import *


def check_repeating_digits(string):
    for i in range(len(string) - 2):
        if string[i] == string[i + 1] == string[i + 2]:
            return True
    return False


k = 0
for w in product('012345678', repeat=7):
    word = ''.join(w)
    if word[-1] not in '347' and word[0] != '0' and check_repeating_digits(word):
        k += 1
print(k)
