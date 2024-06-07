for n in range(1, 1000): 
    s = '>' + 13*'0' + n*'1' + 6*'3'
    while '>0' in s or '>1' in s or '>3' in s: 
        s = s.replace('>0', '12>', 1)
        s = s.replace('>1', '2>', 1)
        s = s.replace('>3', '1>', 1)
    summa = s.count('1') + s.count('2') * 2 + s.count('3') * 3
    if summa == 101:
        print(n)
        break
        