s = open('variant11/24_8959.txt').readline()
s = s.replace('EA', '**').replace('NPC', '***')
kmax = k = 0
for i in s:
    if i == '*':
        k += 1
    else: 
        kmax = max(k, kmax)
        k = 0
print(kmax)
