def f(n):
    n3 = ''
    while n > 0:
        n3 = str(n % 3) + n3
        n = n // 3
    return n3


for n in range(1, 100):
    s = f(n)
    if (s.count('1') + s.count('2') * 2) % 3 == 0:
        s = '2' + s + '2'
    else:
        s += f(((s.count('1') + s.count('2') * 2) % 3) * 2)

    if int(s, 3) > 112:
        print(int(s, 3), n)