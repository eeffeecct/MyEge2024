def f(n):
    n27 = ''
    while n:
        n27 = str(n % 27) + ' ' + n27
        n //= 27
    return n27

for x in '0123456789abcdefghijlklmnop':
    if (int(f'123{x}24', 27) + int(f'135{x}78', 27)) % 26 == 0:
        print((int(f'123{x}24', 27) + int(f'135{x}78', 27)) / 26)

