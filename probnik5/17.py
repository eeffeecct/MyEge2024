s = [int(x) for x in open('probnik5/1005_17.txt')]
maxim = max([x for x in s if x % 10 == 6 and len(str(abs(x))) == 4])
data = []
for i in range(len(s) - 2):
    usl1 = (s[i] % 10 == 6 and len(str(abs(s[i]))) == 4) + (s[i+1] % 10 == 6 and len(str(abs(s[i+1]))) == 4)
    usl2 = s[i] + s[i+1]
    if usl1 >= 1 and usl2 <= maxim:
        data.append(usl2)
print(len(data), max(data))