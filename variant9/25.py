from fnmatch import fnmatch 

for i in range(3255540123, 10**13, 519):
    s = fnmatch(str(i), '32*54?123')
    if s and '0' not in str(s) and len(str(s)) % 2 == 0:
        k = sum(map(int, str(s[:len(str(s)/2)])))
        if 
    
        print(i, i / 519)
