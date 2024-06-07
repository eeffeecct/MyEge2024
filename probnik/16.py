from sys import setrecursionlimit

def f(n):
    if n <= 3:
        return 2024
    elif n > 3:
        return (n + 3) * f(n-2)


setrecursionlimit(3000)
print(f(2025)/f(2021))
