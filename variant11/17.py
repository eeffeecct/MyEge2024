s = [int(x) for x in open('variant11/17_8954.txt')]
maxim = max([x for x in s if hex(x)[-2:] == '0f'])
data = []
for i in range(len(s) - 1):
    usl = (s[i] % 7 == 0) + (s[i+1] % 7 == 0)
    m = s[i] + s[i+1]
    if usl == 1 and m % maxim == 0:
        data.append(m)
print(len(data), max(data))
