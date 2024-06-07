def tr(n):
    n2 = ''
    while n > 0:
        n2 = str(n % 3) + n2
        n //= 3
    return n2


for n in range(1, 1000):
    s = tr(n)
    s += str(n % 3)

    print(int(s, 3))