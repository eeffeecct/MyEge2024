from fnmatch import fnmatch

for n in range(98591, 10**11, 98591):
    if fnmatch(str(n), '12*3?7?51?'):
        print(n, n // 98591)

