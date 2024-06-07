from sys import setrecursionlimit


def f(n):
    if n < 3:
        return 1
    if n > 2 and n % 2 != 0:
        return f(n - 1) + n
    if n > 2 and n % 2 == 0:
        return f(n-3) + 2 * n


setrecursionlimit(3500)
print(f(2048) - f(2041))
