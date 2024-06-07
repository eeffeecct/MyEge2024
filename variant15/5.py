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
        s += '02'
    else: 
        s = '1' + s + '2'
    r = int(s, 3)
    if r <= 167:
        data.append(r)
print(max(data))