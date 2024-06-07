from fnmatch import fnmatch

for n in range(253, 10**8, 253):
    if fnmatch(str(n), '12??15*6'):
        print(n, n // 253)