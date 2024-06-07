def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif 2 <= n <= 4:
        return n
    elif n >= 5 and n % 2 == 0:
        return f(n // 2) + f(n - 1)
    elif n >= 5 and n % 2 == 0:
        return f(n-1)


print(f(25)-f(12))
