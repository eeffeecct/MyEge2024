for n in range(1, 1000):
    s = bin(n)[2:]
    if s[-1] == '0':
        k = s.count('0')
        s += k*'0'
    else:
        b = s.count('1')
        s = b*'1' + s
    if int(s,2) > 2000:
        print(n)
        break
