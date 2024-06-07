from functools import lru_cache


@lru_cache
def f(n):
    if n < 3:
        return 3*n
    elif n > 2 and n % 2 == 0:
        return f(n-2) + f(n-1) - n
    elif n > 2 and n % 2 != 0:
        return f(n-1) - f(n-2) + 2*n


k = 0
for i in range(1, 201):
    try:
        if int((str(f(i))[-1] + str(f(i))[-2])) % 2 == 0:
            k += 1
    except IndexError:
        pass
print(k)
