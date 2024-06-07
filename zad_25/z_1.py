from fnmatch import fnmatch

for n in range(2056, 10**8, 2056):
    if fnmatch(str(n), '234?9?3?376'):
        print(n, n // 2056)

# otvet: 
# 35995708 11158
# 36995768 11468

