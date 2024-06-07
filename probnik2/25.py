from fnmatch import fnmatch


for n in range(98591, 10**11, 98591):
    if fnmatch(str(n), '123??72?1*'):
        print(n, n // 98591)