from sys import setrecursionlimit


def f(n):
    if n > 3000:
        return n
    if n <= 3000 and n % 2 == 0:
        return n + f(n + 1) + 1
    if n <= 3000 and n % 2 != 0:
        return f(n + 2) + 2

setrecursionlimit(3100)
print(f(400000) - f(400003))