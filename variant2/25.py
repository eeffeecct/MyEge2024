from fnmatch import fnmatch

for n in range(1, 10**8, 2084):
    if fnmatch(str(n), '*1?542?'):
        print(n, n // 2084)