s = [int(x) for x in open('aintens/variant1/17.txt')]
minim = min([abs(x) for x in s if str(abs(x))[-2:]=='17'])
data = []
for i in range(len(s) - 2):
    summa = s[i] + s[i+1] + s[i+2]
    n1 = str(s[i])[-1]
    n2 = str(s[i+1])[-1]
    n3 = str(s[i+2])[-1]
    if ((n1 == n2) or (n1 == n3) or (n2 == n3)) and summa % minim == 0:
        data.append(summa)
print(len(data), max(data))
