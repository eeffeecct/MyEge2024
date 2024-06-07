s = open('variant10/24_11465.txt').readline()

k = kmax = 0
for i in range(len(s) - 1):
    if (s[i] in 'ABC' and s[i+1] not in 'ABC') or (s[i] in '89' and s[i+1] not in '98') :
        k += 1
    else:
        kmax = max(kmax, k)
        k = 0

print(kmax+1)
