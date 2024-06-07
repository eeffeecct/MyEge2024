from sys import setrecursionlimit
def f(n):
    if n < 11:
        return n
    else: 
        return n + f(n - 1)
setrecursionlimit(4000)
print(f(2024) - f(2021))