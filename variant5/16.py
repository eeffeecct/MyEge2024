def f(n):
    if n>=2025:
        return n
    else:
        return n + f(n + 2)
print(f(2022) - f(2023))
