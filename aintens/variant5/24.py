s = open('aintens/variant5/24_12254.txt').readline()
k = 1
kmax = 0
for i in range(1, len(s)): 
    if s[i-1] + s[i] in ('QR', 'RS', 'SQ'):
        k += 1
        kmax = max(kmax, k)
    else : k = 1
print(kmax)