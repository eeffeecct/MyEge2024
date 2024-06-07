# Вася составляет 5-буквенные коды из букв К, А, Л, И, Й. Каждую букву нужно использовать ровно 1 раз, при этом код
# не может начинаться с буквы Й и не может содержать сочетания ИА. Сколько различных кодов может составить Вася?

from itertools import *

k = 0
for w in permutations('калий'):
    word = ''.join(w)
    if word[0] != 'й' and 'иа' not in word:
        k += 1
print(k)