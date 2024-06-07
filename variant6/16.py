from sys import setrecursionlimit

def f(n):
    if n < 5:
        return n
    else:
        return n +f(n-1)


setrecursionlimit(2000)
print(f(1234) - f(1230))
