
for n in range(3, 10001):
    s = '5' + n * '2'
    while '52' in s or '2222' in s or '1112' in s:
        if '52' in s:
            s = s.replace('52', '11', 1)
            s = s.replace('2222', '5', 1)
        else:
            s = s.replace('1112', '2', 1)
    if s.count('5') * 5 + s.count('2') * 2 + s.count('1') == 1685:
        print(n)