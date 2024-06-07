s = open('variant14/24_16333.txt').readline()

s = s.replace('Q', 'W').replace('R', 'W').replace('2', '1').replace('4', '1')
k = kmax = 0
print(s)
for i in range(len(s) - 2): 
    if s[i] != s[i+1]:
        k += 1
    else: 
        kmax = max(kmax, k)
        k = 0
print(k)