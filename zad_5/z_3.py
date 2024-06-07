for n in range(1, 1000):
    s = bin(n)[2:]
    if s.count('1') > s.count('0'):
        s += '1'
    else:
        s += '0'
    if int(s, 2) > 80:
        print(int(s, 2))
        break

# otvet: 82