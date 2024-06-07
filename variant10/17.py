s = [int(x) for x in open('variant10/17_11460.txt')]
maxim = max([i for i in s if str(abs(i))[0] == '8'])
data = []
for i in range(len(s) - 2):
    usl1 = (str(abs(s[i]))[0] == '6') + (str(abs(s[i+1]))[0] == '6') + (str(abs(s[i+2]))[0] == '6')
    summa = s[i] + s[i+1] + s[i+2]
    if usl1 <= 1 and summa >= maxim:
        data.append(summa)
print(len(data), min(data))

