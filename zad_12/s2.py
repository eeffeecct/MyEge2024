data = []
for i in range(1, 1000):
    s = bin(i)[2:]
    if s.count('1') % 2 == 0:
        s = '1' + s[2:] + '0'
    else:
        s = '11' + s[2:] + '1'

    if int(s, 2) > 49:
        data.append((int(s, 2), i))
print(min(data))



