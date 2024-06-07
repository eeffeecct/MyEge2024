s = open('variant8/24.txt').readline()

s = s.replace('NPONPONPO', '*')
s = s.replace('PNOPNOPNO', '*')

data = []
k = 0
for i in range(len(s) - 1):
    if s[i] == '*': 
        k += 1
    else:
        data.append(k)
        k = 0
print(max(data))
