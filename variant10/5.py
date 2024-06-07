def f(n):
    n3 = ''
    while n:
        n3 = str(n % 3) + n3
        n //= 3
    return n3


for i in range(1, 1000):
    s = f(i)
    if i % 2 == 0:
        s = '1' + s + '00'
    else:
        s += f(s.count('1'))
    if int(s, 3) > 168:
        print(i)
        break
