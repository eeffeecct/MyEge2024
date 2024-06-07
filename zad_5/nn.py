data = set()
for n in range(1, 1000):
    s = bin(n)[2:]
    if s.count('1') > s.count('0'):
        s += '11'
    elif s.count('1') == s.count('0') or s.count('0') > s.count('1'):
        s += '0'
    if int(s, 2) > 80:
        data.add(int(s, 2))
        print(min(data))




