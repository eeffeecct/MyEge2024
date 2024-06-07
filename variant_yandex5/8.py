from itertools import * 

k = 0
for i in product('воздух', repeat=5):
    s = ''.join(i)

    if s.count('у') == 1 and s.count('о') == 0 and (('ув' not in s and 'ву' not in s) and ('ху' not in s and 'ух' not in s)):
        k += 1
    if s.count('о') == 1 and s.count('у') == 0 and (('ов' not in s and 'во' not in s) and ('хо' not in s and 'ох' not in s)):
        k += 1
print(k)