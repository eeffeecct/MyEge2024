data = []
for n in range(3, 10000):
    s = '3' + '5' * n
    while '33' in s or '555' in s or '7777' in s:
        if '33' in s:
            s = s.replace('33', '5', 1)
        elif '555' in s:
            s = s.replace('555', '77', 1)
        elif '7777' in s:
            s = s.replace('7777', '333', 1)
        summa = s.count('7') * 7 + s.count('5') * 5 + s.count('3') * 3
        data.append(summa)

print(max(data))
