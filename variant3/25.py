from fnmatch import fnmatch

for n in range(23, 10**9, 23):
    if fnmatch(str(n), '12345?7?8'):
        print(n, n // 23)
