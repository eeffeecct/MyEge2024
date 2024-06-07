data = []
for i in range(1, 1000):
    s = bin(i)[2:]
    if i % 2 == 0:
        s += '0'
        s = '1' + s
    else:
        s = '11' + s + '11'

    if int(s, 2) > 52:
        data.append(int(s, 2))

print(min(data))