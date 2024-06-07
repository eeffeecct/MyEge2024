from sys import setrecursionlimit
def f(x, y):
    if x == y:
        return 1
    elif x < y and x == 17:
        return 0
    else:
        return f(x-1, y) + f(x-4, y) + f(x % 3, y)

setrecursionlimit(10000)
print(f(39, 10) * f(10, 5))