from fnmatch import fnmatch

for n in range(98591, 10**12, 98591):
    if fnmatch(str(n), '12?3*456??9'):
        print(n, n // 98591)