from functools import lru_cache

@lru_cache
def f(x, y):
    data3 = []
    data5 = []
    if x % 3 == 0:
        data3.append(x)
    if x % 5 == 0:
        data5.append(x)
    if x == y and len(data3) == len(data5):
        return 1
    elif x > y:
        return 0
    else:
        return f(x+1, y) + f(x + 4, y) + f(x * 3, y)


print(sum(map(int, str(f(1, 180)))))
