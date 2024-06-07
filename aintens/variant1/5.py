for n in range(8, 1000):
    s = bin(n)[2:]
    if n % 4 == 0: 
        s = s[:-3] + ''.join('0' if i == '1' else '1' for i in s[-3:])
    else: 
        s = ''.join('0' if i == '1' else '1' for i in s[:3])+ s[3:]
    if int(s, 3) > 360:
        print(n)
        break
