from sys import setrecursionlimit
from functools import lru_cache

@lru_cache
def f(x):
    if x <= 2:
        return 2**x
    elif x > 2 and x % 2 == 0:
        return f(x // 2)
    else:
        return f(x+1) + f(x - 4)
    

setrecursionlimit(1500)
print(f(4202))
