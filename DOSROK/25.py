from fnmatch import *

for i in range(2024, 10**10, 2024):
    if fnmatch(str(i), '1*2322?2'):
        print(i, i / 2024)
