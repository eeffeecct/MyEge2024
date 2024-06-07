# from fnmatch import fnmatch

# for n in range(2024, 10**10, 2024):
#     if fnmatch(str(n), '19?71*32?'):
#         print(n, n // 2024)


for a in range(10):
    for b in range(10):
        for c in range(10):
            x = int(f'12{a}345{b}67089{c}')
            if x % 206 == 0:
                print(x, x // 206)