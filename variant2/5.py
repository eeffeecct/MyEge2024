for i in range(1, 1000):
    s = bin(i)[2:]
    if s.count('1') % 2 == 0:
        s += '1'
        s = s[:-2] + '01'
    else:
        s += '10'
        s = '1' + s[2:]
    if int(s, 2) < 100:
        print(int(s, 2))