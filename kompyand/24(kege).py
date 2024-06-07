s = open('kompyand/24kege.txt').readline()
# бццбц
b = 'TUVWXYZ'
c = '0123456789'
k = kmax = 0
for n in range(0, 5): 
    for i in range(n, len(s) - 6, 5): 
        
        if s[i] in b and s[i+1] in c and s[i+2] in c and s[i+3] in b and s[i+4] in c :
            k += 5
            kmax = max(k, kmax)
        else: 
            k = 0
print(kmax)
