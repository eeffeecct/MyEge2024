kmax = 0
for n in range(3, 10000):
    s = '5' + n*'7'
    k = 0
    while '33' in s or '555' in s or '777' in s:
        if '33' in s :
            s = s.replace('33','5',1)
        if '555' in s: 
            s = s.replace('555', '77', 1)
        if '777' in s: 
            s = s.replace('777', '3', 1)

    k = sum(map(int, s))
    kmax = max(k, kmax)
    
print(kmax)