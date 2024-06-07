s = [int(x) for x in open('DOSROK/17_15333.txt')]
maxim = max([i for i in s if i % 19 == 0])
data = []
for i in range(len(s) - 1):
    if s[i] > maxim or s[i+1] > maxim:
        data.append(s[i] + s[i+1])
print(len(data), max(data))
