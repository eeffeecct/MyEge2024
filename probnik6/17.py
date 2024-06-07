s = [int(x) for x in open('probnik6/17.txt')]
maxim = max([x for x in s if x % 100 == 63])
data = []
for i in range(len(s) - 2):
    summa = s[i] + s[i+1] + s[i+2]
    prois = s[i] * s[i+1] * s[i+2]
    res = (s[i] % maxim == 0) + (s[i+1] % maxim == 0) + (s[i+2] % maxim == 0)
    if res == 1 and summa < prois: 
        data.append(summa)
print(len(data), max(data))
