def f(n):
    n9 = ''
    while n: 
        n9 = str(n % 9) + n9
        n //= 9
    return n9

n = 2*729**333 + 2*243**334-81**335+2*27**336-2*9**337-338

print(len(f(n)) - f(n).count('0'))
