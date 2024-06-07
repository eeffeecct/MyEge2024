def f(n):
    n3 = ''
    while n:
        n3 = str(n % 3) + n3
        n //= 3
    return n3


k = 0
for n in range(1, 1000000):
    s = f(n)
    if n % 5 == 0:
        s += s[-3:]
    else:
        s += f(n % 5 * 5)
    if 1000 <= int(s, 3) <= 9999:
        k += 1
print(k)
