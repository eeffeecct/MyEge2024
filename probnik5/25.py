from fnmatch import *

for n in range(98591, 10**11, 98591):
    if fnmatch(str(n), '12*3??751?'):
        print(n, n // 98591)