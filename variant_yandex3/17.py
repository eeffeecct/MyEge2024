s = [int(i) for i in open('17.txt')]
p = max([s[i] for i in range(len(s)) if 100 <= abs(s[i]) <= 999])**3
data = []
for i in range(len(s) - 1):
    usl1 = (sum([int(x) for x in str(abs(s[i]))]) % 5 == 0) + (sum([int(x) for x in str(abs(s[i+1]))]) % 5 == 0)
    usl2 = abs(s[i]**2 - s[i+1]**2)
    if (usl1 == 1) and (usl2 > p):
        data.append(s[i] + s[i + 1])
print(len(data), max(data))