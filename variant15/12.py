for n in range(1, 100):
    s = '>' + n * '4' + 25 * '5' + n * '6'
    while '>4' in s or '>5' in s or '>6' in s: 
        s = s.replace('>4', '55>')
        s = s.replace('>5', '5>4')
        s = s.replace('>6', '4>5')

    if 10 * (s.count('4') + s.count('6')) == s.count('5'):
        print(n)
        break