for n in range(1, 100):
    s = n * '0' + '1'
    while '01' in s:
        if '1' in s:
            s = s.replace('1', '10', 1)
        if '01' in s:
            s = s.replace('01', '1000', 1)
    if 100 <= s.count('0') <= 999:
        print(n)
        break