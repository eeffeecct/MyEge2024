from fnmatch import *

for s in range(2024, 10**10, 2024):
    if fnmatch(str(s), '10*2024?'):
        print(s, s // 2024)
