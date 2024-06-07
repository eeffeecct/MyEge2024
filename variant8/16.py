from sys import setrecursionlimit
def f(n):
    if n == 1:
        return 1
    elif n > 1:
        return n - 2 + f(n - 1)
setrecursionlimit(4000)
print(f(2024) - f(2022))
