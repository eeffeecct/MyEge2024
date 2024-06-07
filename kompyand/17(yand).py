s = [int(x) for x in open('kompyand/17yand.txt')]
maxim = max([x for x in s if x > 0 and len(str(x)) == 5 and str(x)[-2:]== '17'])
data = []
for i in range(len(s) - 2):
    usl = (str(abs(s[i]))[-2:]=='17') + (str(abs(s[i+1]))[-2:]=='17') + (str(abs(s[i+2]))[-2:]=='17') 
    summa = abs(s[i]) + abs(s[i+1]) + abs(s[i+2])
    if usl >= 1 and summa <= maxim:
        data.append(s[i] + s[i+1] + s[i+2])
print(len(data), min(data))
