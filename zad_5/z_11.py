for n in range(1, 1000):
    s = bin(n)[2:]
    if s.count('1') % 2 == 0:
        s += '0'
        s = '10' + s[2:]
    else:
        s += '1'
        s = '11' + s[2:]
    if int(s, 2) < 47:
        print(n)

# otvet: 30
