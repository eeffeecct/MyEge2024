from functools import *

@lru_cache
def f(x,y):
    if x == y:
        return 1
    elif x > y or x == 100:
        return 0
    s = 0
    if x % 10 != 0:
        s += f(x + x % 10, y)
    if x % 68 != 0:
        s += f(x + x % 68, y)
    s += f(x**2, y)
    return s
    

print(f(2, 68) * f(68, 680))