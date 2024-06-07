from fnmatch import fnmatch

k = 0
for i in range(8, 680001, 8):
    if (str(i), '1*2*'):
        k += 1
print(k)
