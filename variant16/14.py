def f(n):
    n2 = ''
    while n:
        n2 = str(n % 64) + n2
        n //= 64
    return n2

n = f(7*512**3200+6*256**3100-5*64**3000-4*8**2900-1542)
print(n.count('0'))