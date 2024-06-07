for i in range(1, 1000):
    s = bin(i)[2:]
    if s.count('1') % 3 == 0:
        s += s[2:]
    else:
        s = str(3 * bin(s.count('1') % 3)[2:]) + s

    if int(s, 2) < 60:
        print(i)