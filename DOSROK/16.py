from sys import setrecursionlimit


def f(n):
    if n <= 7:
        return 1
    else:
        return n + 2 + f(n - 1)
setrecursionlimit(3000)
print(f(2024) - f(2020))
