from fnmatch import *

for n in range(98, 10**12, 98):
    if n % 392 != 0 and fnmatch(str(n), '98?7*93?24'):
        print(n, n // 98)
