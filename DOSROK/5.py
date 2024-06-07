for n in range(1, 1000):
    s = bin(n)[2:]
    if n % 2 == 0:
        s += '01'
    else:
        s = '1'+ s + '1'
    if int(s, 2) > 156:
        print(n)
        break
    