def f(n):
    if n <= 1:
        return n
    elif n > 1 and n % 2 == 0:
        return 1 + f(n / 2)
    elif n > 1 and n % 2 != 0:
        return 1 + f(n - 2)


a = 0
while f(a) != 16:
    a += 1
print(a)
# otvet: 31
