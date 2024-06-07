from fnmatch import fnmatch

for n in range(2023, 10**8, 2023): 
    if fnmatch(str(n), '671??1*'):
        print(n, n//2023)
