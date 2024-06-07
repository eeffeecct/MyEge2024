data = []
for n in range(3, 10001):
    s = '3' + n * '7'
    while '3333' in s or '555' in s or '777' in s:
        if '3333' in s:
            s = s.replace('3333', '5', 1)
        elif '555' in s:
            s = s.replace('555', '77', 1)
        elif '777' in s:
            s = s.replace('777', '3')
        data.append(s.count('3') * 3 + s.count('5') * 5 + s.count('7') * 7)
print(max(data))