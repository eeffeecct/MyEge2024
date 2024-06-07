def f(n):
    n9 = ''
    while n:
        n9 = str(n % 9) + n9
        n //= 9
    return n9

n = 361 * 2349**84 - 89**192 + 1953**481 * 4843**151
print(f(n).count('5'))