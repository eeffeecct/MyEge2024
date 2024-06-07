def f(n):
    n3 = ''
    while n > 0:
        n3 = str(n % 3) + n3
        n = n // 3
    return n3


data = set()
for n in range(10, 100):
    s = f(n)
    if n % 3 == 0:
        s = s[:-2] + '12'
    else:
        s += f((n % 3) * 5)
    data.add(int(s, 3))

print(len(data))
