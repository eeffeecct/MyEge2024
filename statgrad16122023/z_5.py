for n in range(4,1000000):
    s = bin(n)[2:]

    if n % 2 == 0:
        s = s + s[-2] + s[-1]
    elif n % 2 != 0:
        s = '1' + s
        s += '0'
    if int(s, 2) < 100:
        print(n)