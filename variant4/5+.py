for n in range(1, 1000):
    s = bin(n)[2:]
    s1 = ''
    for i in s:
        if i == '0':
            s1 += '1'
        else:
            s1 += '0'
    for j in s1:
        if j == '0':
            s1=s1[0:]
    s1 = '1' + s1
    if s1.count('1') % 2 != 0:
        s1 += '1'
    else:
        s1 += '0'
    print(s1, '/')
    if int(s1, 2) > 180:
        print(n)
        break