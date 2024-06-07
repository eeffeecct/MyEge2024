def f(n):
    n8 = ''
    while n: 
        n8 = str(n % 8) + n8
        n //= 8
    return n8


for x in range(1,10):
    s = int(f'{x}1{x}', 16) + int(f'{x}3{x}3', 8)
    print(s, x)
