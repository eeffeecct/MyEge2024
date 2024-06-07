s = open('variant_yandex4/24.txt').readline()
k = kmax = 0

for i in range(len(s) - 1): 
    if (s[i] in 'KLMN' and s[i+1] not in 'KLMN') or (s[i] in 'AEOU' and s[i+1] not in 'AEOU'):
        k += 1
    else: 
        kmax = max(kmax, k)
        k = 0

print(kmax+1)
