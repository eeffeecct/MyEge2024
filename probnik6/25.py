from fnmatch import *

for n in range(2735, 10**9, 2735):
    if fnmatch(str(n), '17*2?13?'):
        print(n, n //2735)