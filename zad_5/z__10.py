for n in range(1, 1000):
    s = bin(n)[2:]
    s += s[-1]
    if (bin(n)[2:]).count('1') % 2 == 0:
        s += '0'
    else:
        s += '1'
    if s.count('1') % 2 == 0:
        s += '0'
    else:
        s += '1'
    if int(s, 2) > 136:
        print(n)
        break


