def f(n):
    n13 = ''
    while n:
        n13 = str(n % 13) + n13
        n //= 13
    return n13

n = int(f'9{x}AB', 13) + int(f'')
