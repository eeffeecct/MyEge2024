s = open('DOSROK/24_15339.txt').readline()
k = kmax = 0
for i in range(len(s) - 1): 
    if (s[i] in 'ABC' and s[i+1] not in 'ABC') or (s[i] in '6789' and s[i+1] not in '6789'):
        k += 1
        kmax = max(k, kmax)
    else:
        k = 0

print(kmax + 1)
