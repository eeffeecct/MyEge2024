data = []
for n in range(1000, 10001):
    s = str(n)
    data.append(int(s[0]) + int(s[1]))
    data.append(int(s[1]) + int(s[2]))
    data.append(int(s[2]) + int(s[3]))
    data.sort()
    data.pop(0)
    if int(''.join(map(str, data))) == 126:
        print(n)
    data.clear()
