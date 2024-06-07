s = [int(x) for x in open('variant_yandex4/17.txt')]
maxim = max([i for i in s if i % 21 == 0])
data = []
for i in range(len(s) - 1):
    usl = (s[i] > maxim) + (s[i+1] > maxim)
    if usl >= 1:
        data.append(s[i] + s[i+1])
print(len(data), min(data))
