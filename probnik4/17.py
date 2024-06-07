s = [int(x) for x in open('probnik4/17.txt')]
minim = min([x for x in s if len(str(x)) == 3 and str(x)[-1] == '5'])
data = []
for i in range(len(s) - 2):
    usl1 = (len(str(s[i])) == 3) + (len(str(s[i+1])) == 3)
    summa = s[i] + s[i+1]
    if usl1 >= 1 and summa % minim == 0:
        data.append(summa)
print(len(data), max(data))