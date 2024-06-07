s = open('variant13/24_12111.txt').readline()
kmax = k = 0

for i in range(3): 
    for j in range(i, len(s) - 2, 3): 
        if s[j:j+3] == 'HPY' or s[j:j+3] == 'NYN':
            k += 1
        else: 
            kmax = max(kmax, k)
            k = 0

print(kmax)