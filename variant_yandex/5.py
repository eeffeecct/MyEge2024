def pyat(n):
    n5 = ''
    while n > 0:
        n5 = str(n % 5) + n5
        n //= 5
    return n5


for n in range(1, 1000):
    s = pyat(n)
    if n % 25 == 0:
        s = s[-3:] + s
    else:
        ostat = n % 25
        ostat = pyat(ostat)
        s += ostat
    if int(s, 5) > 10000:
        print(n)
        break

