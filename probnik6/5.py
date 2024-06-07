def f(n) : 
    n3 = ''
    while n:
        n3 = str(n % 3) + n3
        n //= 3
    return n3

for n in range(13, 1000):
    s = f(n)
    if n % 4 == 0:
        s = s[1:] + s[:1]
    else: 
        s = s[:-3] + '222'
    if int(s,3) > 360:
        print(n)
        break
