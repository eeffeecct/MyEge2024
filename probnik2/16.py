def f(n):
    if n <= 3:
        return 2023
    else:
        return (n + 1) * f(n - 3)


print(f(2025)/f(2019))