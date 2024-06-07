s = [int(x) for x in open('variant13/17_12106.txt')]
minim = min([i for i in s if i > 0 and i % 117 == 0])

data = []
for i in range(len(s) - 2):
    usl = (s[i] < 0) + (s[i+1] < 0)
    summa = s[i] + s[i+1]
    if usl == 1 and summa % minim == 0:
        data.append(s[i]**2 + s[i+1]**2)
print(len(data), min(data))
