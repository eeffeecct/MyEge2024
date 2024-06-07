s = [int(x) for x in open('aintens/variant4/17_15333.txt')]
maxim = max([x for x in s if int(x) % 19 == 0])
data = []
for i in range(len(s) - 1):
    usl = (s[i] > maxim) + (s[i+1] > maxim)
    if usl >= 1:
        data.append(s[i] + s[i+1])
print(len(data), max(data))
