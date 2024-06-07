def to4(n):
    n4 = ''
    while n:
        n4 = str(n % 4) + n4
        n //= 4
    return n4


for i in range(200, 1, -1):
    if to4(i)[-3:] == '123':
        print(i)