for n in range(4, 10000):
    s = '3' + n*'5'
    while '25' in s or '355' in s or '555' in s:
        if '25' in s:
            s = s.replace('25', '5', 1)
        elif '355' in s:
            s = s.replace('355', '52', 1)
        elif '555' in s:
            s = s.replace('555', '3', 1)
    if len(s) == s.count('5'):
        print(n)
        break
