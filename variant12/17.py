s = [int(x) for x in open('variant12/17_11887.txt')]
maxim = max([i for i in s if abs(i) % 100 == 68])

data = []
for i in range(len(s) - 3):
    usl1 = (len(str(abs(s[i]))) == 2) + (len(str(abs(s[i+1]))) == 2) + (len(str(abs(s[i+2]))) == 2) + (len(str(abs(s[i+3]))) == 2)
    summa = s[i] + s[i+1] + s[i+2] + s[i+3]
    if (usl1 == 1 or usl1 == 4) and (summa >= maxim):
        data.append(summa)
print(len(data),max(data))