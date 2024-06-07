def f(n):
    n3 = ''
    while n:
        n3 = str(n % 3) + n3
        n //= 3
    return n3


data = []
for n in range(1, 1000):
    s = f(n)
    if n % 3 == 0:
        s += s[-3:]
    else:
        s += f(n % 3 * 5)
    if int(s, 3) > 133:
        data.append(int(s, 3))
print(min(data))
