s = [int(x) for x in open('aintens/variant5/17_12249.txt')]
maxim = max([x for x in s if len(str(abs(x))) == 5 and str(abs(x))[-1] == '3'])
data = []
for i in range(len(s) - 2): 
    usl = (str(abs(s[i]))[-1] == '3')+(str(abs(s[i+1]))[-1] == '3')+(str(abs(s[i+2]))[-1] == '3')
    summa = s[i] + s[i+1] + s[i+2]
    if usl >= 1 and summa <= maxim:
        data.append(summa)
print(len(data), max(data))