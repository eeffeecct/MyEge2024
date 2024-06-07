s = open('aintens/variant1/24.txt').readline().replace('L', '.').replace('O', '.').replace('V', '.').replace('E', '.').split('.')
l = 0
maxlen = 0
k = 0

for r in range(len(s)):
    if s[r] == '.': k += 1
    while k > 1: 
        if s[l] == '.': k = 0
        l += 1 
    maxlen = max(maxlen, r-l+1)
print(maxlen)