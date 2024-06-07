def f7(n):
    n7 = ''
    while n:
        n7 = str(n % 7) + n7
        n //= 7
    return n7

data = []
for n in range(1, 1000):
    s = f7(n)
    if sum(map(int, s)) % 2 == 0: 
        s += '0'
    else: 
        s = '6' + s[1:]
    if int(s,7) < 119: 
        data.append(int(s,7))

print(max(data))


