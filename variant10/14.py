def f(n):
    n5 = ''
    while n:
        n5 = str(n % 5) + n5
        n //= 5
    return n5

for x in range(1, 100):
    n = f(4*625**1920 + 4*125**x - 4*25**1940 - 3*5**1950 - 1960)
    if n.count('0') == 1891:
        print(x)
        break
    