def f(n):
    n3 = ''
    while n: 
        n3 = str(n % 3) + n3
        n //= 3
    return n3


for n in range(100,1,-1):
    s = f(n)
    if n % 3 == 0:
        s = '1' + s + '02'
    else: 
        s += f((n%3)*4)
    if int(s,3) < 199: 
        print(n)
        break