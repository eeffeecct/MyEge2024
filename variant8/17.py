s = [int(x) for x in open('variant8/17.txt')]
m = max([j for j in s if str(j)[-3:] == '121'])
data = []
for i in range(len(s) - 2):
    summa = s[i] + s[i+1] + s[i+2]
    if summa < m and ((len(str(abs(s[i]))) == 4 and s[i] % 2 == 0) or (len(str(abs(s[i+1]))) == 4 and s[i+1] % 2 == 0) or (len(str(abs(s[i+2]))) == 4 and s[i+2] % 2 == 0) ):
        data.append(s[i] + s[i+1] + s[i+2])
print(len(data), max(data))
